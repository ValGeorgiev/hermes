# HermesGift
Official Hermes Gift repository

## Table of Contents
1. [Application Configurations](https://github.com/ValentinAlexandrovGeorgiev/hermes#application-configurations)
2. [Technology stack](https://github.com/ValentinAlexandrovGeorgiev/hermes#technology-stack)
3. [Routing](https://github.com/ValentinAlexandrovGeorgiev/hermes#routing)
4. [Data API](https://github.com/ValentinAlexandrovGeorgiev/hermes#data-api)
5. [Backend Endpoints](https://github.com/ValentinAlexandrovGeorgiev/hermes#backend-endpoints)
6. [Git Flow](https://github.com/ValentinAlexandrovGeorgiev/hermes#git-flow)

## Application Configurations


## Technology stack
Main languages & libraries :
- React
- Redux
- Webpack
- Babel
- react-router
- lodash
- Django
- Postgre


## Routing
Route | Description | Old page
------|-------------|---------
/ | Home page | http://hermesgift.bg/
/products | Products page with | http://hermesgift.bg/index.php/categories/sklad
/products/:category | Products from category | http://hermesgift.bg/index.php/categories/sklad/mobile-accessories
/services | Services page | http://hermesgift.bg/index.php/nashatapechatnitsa
/service/:serviceid | Service details page | http://hermesgift.bg/index.php/nashatapechatnitsa/item/tamponen-pechat
/for-us | For us & Contacts page | http://hermesgift.bg/index.php/for-us
/search/products/:keyword | Search page with specific keyword | http://hermesgift.bg/index.php/component/virtuemart/search?keyword=180-01&limitstart=0&option=com_virtuemart&view=category
/catalogs | Catalogs page | http://hermesgift.bg/index.php/catalogs


## DATA API

###### Product
> - **name**: Product name
> - **description**: Product description
> - **product_id**: Hermes product ID
> - **client_id**: Client product ID
> - **category_id**: Category ID (ForeignKey)
> - **price**: Price
> - **currency**: USD/lv
> - **image_link**: link to cloudinary
> -	**online**: true/false
> - **views**: Number of views


###### Category
Category contain products [example](http://hermesgift.bg/index.php/categories/sklad)
>	- **name**: Category name
> - **value**: Category value (for links)
> - **products**: Products in the category
> - **parent_category**: Parent category
> - **image_link**: Category front image
> - **online**: true/false


###### Catalog
PDF Catalogs, [examples](http://hermesgift.bg/index.php/catalogs)
> - **name**: Catalog name
> - **image_link**: Catalog front image (link to cloudinary)
> - **link**: Link to catalog pdf
> - **online**: true/false


###### Assets
Texts [Example 1](http://hermesgift.bg/index.php/for-us) , [Example 2](http://hermesgift.bg/index.php/nashatapechatnitsa)
> - **title**: Asset title
> - **body**: Asset body (HTML or simple text)
> - **asset_id**: Unique asset id
> - **image_link**: Asset front image
> - **online**: true/false

##### Site
Site configurations. Example: Which assets to be displayed on http://hermesgift.bg/index.php/nashatapechatnitsa And other configurations
> - **services**: Array with assets values

## Backend Endpoints

**Product:**

**Get product:**

method: **GET** </br>
endpoint: **/api/product/{id}** </br>
response: </br>
```
{
	name: String,
	description: String,
	price: String,			// 22,00 лв
	product_id: String,
	image_link: String,
	category_id: ForeignKey
}
```

error response:
```
{
    status_code: 404,
    "detail": "Not Found"
}
```

description: </br>
- If everything is OK with this product, the API returns status 200 and product data. </br>
- If product is not found, the API returns status 404 and NOT_FOUND status_code </br>
- If product is offline, the API returns status 404 and NOT_FOUND status_code </br>
</br>

**Get products from category:**

method: **GET** </br>
endpoint: **/api/products/{category_name}** </br>
response: </br>
```
{
	products: [
		{
			name: String,
			price: String,
			image_link: String,
			product_id: String
		},
		{
			name: String,
			price: String,
			image_link: String,
			product_id: String
		}
	],
	count: Number
}
```
error response: </br>
```
{
    status_code: 404,
    "detail": "Not Found"
}
```

optional parameters: </br>
**count**: how many products to return. Example: when we want to implement pagination (page size is this count) </br>
**start**: from which product to start the search. Same Example ^ </br>

description: </br>
If category is not found, the API returns status 404 and NOT_FOUND status_code </br>
Return only online products </br>

</br>
</br>

**Category:** </br>

**Get categories:** </br>

method: **GET** </br>
endpoint: **/api/categories** </br>
response: </br>
```
{
	categories: [
		{
			name: String,
			value: String,
			category_img: String
		},
		{
			name: String,
			value: String,
			category_img: String
		}
	],
	count: Number
}
```

description: </br>
Returns only online categories </br>
</br>

**Catalog:** </br>

**Get catalogs:** </br>

method: **GET** </br>
endpoint: **/api/catalogs** </br>
response: </br>
```
{
	catalogs: [
		{
			name: String,
			image_link: String,
			link: String
		},
		{
			name: String,
			image_link: String,
			link: String
		}
	],
	count: Number
}
```
description: </br>
Returns only online catalogs </br>
</br>

**Asset:** </br>

method: **GET** </br>
endpoint: **/api/asset/{asset_id}** </br>
response: </br>
```
{
	title: String,
	body: String,
	asset_id: String,
	image_link: String
}
```

error response: </br>
```
{
    status_code: 404,
    "detail": "Not Found"
}
```

description: </br>
Return only online asset </br>
Body is a simple text or html with tags </br>
</br>

**Sites:** </br>

**Get site configuration** </br>

method: **GET** </br>
endpoint: **/api/site/{config}** </br>
Example response: </br>
```
{
	services: [
		Asset,
		Asset
	]
}
```
error response: </br>
```
{
    status_code: 404,
    "detail": "Not Found"
}
```

description: </br>
Return only online assets </br>
Return only the configuration which you search ({config}) </br>


## Git Flow

> - **master** - main branch, used only for production builds
> - **dev** - dev branch, used to contains all ready features
> - **local-branch** - dev branch, used to contains a separated feature

```
	Steps when you want to develop a feature.
	1. Pull dev branch
	2. Create a new branch. Example update-en-translations
	3. Switch to your new branch
	4. Commit
	5. When you are ready, push your changes
	6. Go to **hermes** github repository and click "Create a pull request" button
	7. Add title and description
	8. Wait for review approval and merge
```
