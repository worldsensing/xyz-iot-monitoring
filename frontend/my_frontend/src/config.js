console.log('Running in mode: ' + process.env.REACT_APP_MODE)

const dev = {
  services: {
    api_device: {
      url: 'http://localhost:5001/devices'
    },
    api_device_category: {
      url: 'http://localhost:5001/device-categories'
    },
    api_event: {
      url: 'http://localhost:5001/events'
    },
    api_business_rule: {
      url: 'http://localhost:5001/business-rules'
    },
    grafana: {
      url: 'http://localhost:3001'
    },
    nodered: {
      url: 'http://localhost:1880'
    }
  }
}

const prod = {
  services: {
    api_device: {
      url: 'http://localhost:8000/api/devices'
    },
    api_device_category: {
      url: 'http://localhost:8000/api/device-categories'
    },
    api_event: {
      url: 'http://localhost:8000/api/events'
    },
    api_business_rule: {
      url: 'http://localhost:8000/api/business-rules'
    },
    grafana: {
      url: 'http://localhost:8000/grafana/'
    },
    nodered: {
      url: 'http://localhost:8000/nodered/'
    }
  }
}

const config = process.env.REACT_APP_MODE === 'production' ? prod : dev

export default config
