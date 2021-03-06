from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import format_html
from django.template.response import TemplateResponse
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportMixin
from import_export.resources import ModelResource
from import_export.forms import ConfirmImportForm
from .models import Category, Product, Catalog, Asset, Site, Item
from .forms import ProductsImagesForm, CatalogForm
from .utils import get_cloudinary_img_or_default
from .exceptions import ImportExportMissingCategory
import cloudinary
try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class ProductResource(ModelResource):

    class Meta:
        model = Product

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        last_obj = Product.objects.last()
        self.id_for_product = last_obj.id if last_obj else 0

    def before_import_row(self, dataset, **kwargs):
        existing_product =\
            Product.objects.filter(product_id=dataset['product_id']).first()
        category = Category.objects.filter(name=dataset['category']).first()

        if existing_product:
            dataset['id'] = existing_product.pk
        else:
            self.id_for_product += 1
            dataset['id'] = self.id_for_product

        try:
            dataset['category'] = category.category_id
        except AttributeError:
            raise ImportExportMissingCategory()

        dataset['image_link'] =\
            get_cloudinary_img_or_default(dataset['image_name'])

        super().before_import_row(dataset, **kwargs)


class ProductAdmin(ImportExportMixin, admin.ModelAdmin):

    list_display = ('name', 'description', 'category', 'delete_product')
    search_fields = ['name', 'product_id']
    resource_class = ProductResource

    def delete_product(self, obj):
        return format_html('<a class="btn" href="/admin/API/'
                           'product/{}/delete/">Delete</a>', obj.id)

    def upload_images_cloudinary(self, request):
        for file in request.FILES.getlist('images'):
            file_name = file.name.split('.')[0]
            cloudinary.uploader.upload(file, public_id=file_name)

    def import_action(self, request, *args, **kwargs):
        '''
        Perform a dry_run of the import to make sure the import will not
        result in errors.  If there where no error, save the user
        uploaded file to a local temp file that will be used by
        'process_import' for the actual import.
        '''
        resource = self.get_import_resource_class()(**self.get_import_resource_kwargs(request, *args, **kwargs))

        context = {}

        import_formats = self.get_import_formats()
        form = ProductsImagesForm(import_formats,
                                  request.POST or None,
                                  request.FILES or None)

        if request.POST and form.is_valid():
            input_format = import_formats[
                int(form.cleaned_data['input_format'])
            ]()
            import_file = form.cleaned_data['import_file']
            # first always write the uploaded file to disk as it may be a
            # memory file or else based on settings upload handlers
            tmp_storage = self.get_tmp_storage_class()()
            data = bytes()
            for chunk in import_file.chunks():
                data += chunk

            tmp_storage.save(data, input_format.get_read_mode())
            self.upload_images_cloudinary(request)

            # then read the file, using the proper format-specific mode
            # warning, big files may exceed memory
            try:
                data = tmp_storage.read(input_format.get_read_mode())
                if not input_format.is_binary() and self.from_encoding:
                    data = force_text(data, self.from_encoding)
                dataset = input_format.create_dataset(data)
            except UnicodeDecodeError as e:
                return HttpResponse(_(u"<h1>Imported file has a wrong encoding: %s</h1>" % e))
            except Exception as e:
                return HttpResponse(_(u"<h1>%s encountered while trying to read file: %s</h1>" % (type(e).__name__, import_file.name)))
            result = resource.import_data(dataset, dry_run=True,
                                          raise_errors=False,
                                          file_name=import_file.name,
                                          user=request.user)

            context['result'] = result

            if not result.has_errors():
                context['confirm_form'] = ConfirmImportForm(initial={
                    'import_file_name': tmp_storage.name,
                    'original_file_name': import_file.name,
                    'input_format': form.cleaned_data['input_format'],
                })

        context.update(self.admin_site.each_context(request))

        context['title'] = _("Import")
        context['form'] = form
        context['opts'] = self.model._meta
        context['fields'] = [f.column_name for f in resource.get_user_visible_fields()]

        request.current_app = self.admin_site.name
        return TemplateResponse(request, [self.import_template_name],
                                context)


class CatalogAdmin(admin.ModelAdmin):
    form = CatalogForm
    search_fields = ['name']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('pdf',)
        return self.readonly_fields


class SiteAdmin(admin.ModelAdmin):
    search_fields = ['config_name']


class AssetAdmin(admin.ModelAdmin):
    search_fields = ['title']


class ItemAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict in order to hide Items from admin index page.
        Assuming that they are for ManyToManyField to Site use only.
        """
        return {}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Asset, AssetAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.site_header = 'Hermes Administration'
admin.site.site_title = 'Hermes Administration'
