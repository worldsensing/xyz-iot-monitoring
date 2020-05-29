// Model of Device that match with the API's Model

class device {
  constructor(name = 'Sample name', category = 'Sample category', location = '') {
    this.name = name
    this.category = category
    this.location = location
  }
}

export default device
