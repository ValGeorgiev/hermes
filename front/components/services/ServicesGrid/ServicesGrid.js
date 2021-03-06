import React, {Component} from 'react'
import PropTypes from 'prop-types'
import { Link } from 'react-router-dom'
import ServiceTile from '../ServiceTile/ServiceTile'
import './servicesgrid.scss'

class ServicesGrid extends Component {
  createChildren () {
  	const {
  	  services,
      lang
  	} = this.props

  	return services.map((service) => {
  	  return (
  	  	<Link to={`/service/${service.query_field}`} key={service.query_field} className='col col-xs-100 col-md-100 col-lg-50'>
  	  	  <ServiceTile service={service} lang={lang} />
  	  	</Link>
  	  )
  	})
  }  

  render () {
    return (
      <div className='col col-xs-100'>
        { this.createChildren() }
      </div>
    )
  }
}

ServicesGrid.defaultProps = {
  services: []
}

ServicesGrid.propTypes = {
  services: PropTypes.array
}

export default ServicesGrid
