import ApiServiceBase from './apiServiceBase.js'
import Config from '../config.js'

class DeviceCategoryAPI extends ApiServiceBase {
  constructor() {
    super()
    this.baseUrl = Config.services.api_device_category.url
  }

  getAllDeviceCategories(priority, callback) {
    this.getFromUrl(
      this.baseUrl,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      priority
    )
  }

  getDeviceCategory(name, priority, callback, errorCallback) {
    this.getFromUrl(
      this.baseUrl + `${name}`,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  addDeviceCategory(deviceCategory, priority, callback, errorCallback) {
    this.postToUrl(
      this.baseUrl,
      deviceCategory,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  updateDeviceCategory(deviceCategory, priority, callback, errorCallback) {
    this.putToUrl(
      this.baseUrl + `${deviceCategory.name}`,
      deviceCategory,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }

  deleteDeviceCategory(name, priority, callback, errorCallback) {
    this.deleteToUrl(
      this.baseUrl + `${name}`,
      (responseJson) => {
        const response = responseJson
        if (response) {
          console.log(response)
          callback(response)
        }
      },
      (errorJson) => {
        const error = errorJson
        if (error) {
          console.log(error)
          errorCallback(error)
        }
      },
      priority
    )
  }
}

export default new DeviceCategoryAPI()
