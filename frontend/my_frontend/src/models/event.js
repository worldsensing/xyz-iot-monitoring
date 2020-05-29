// Model of Event that match with the API's Model

class event {
  constructor(
    id,
    device_name = 'Sample device_name',
    value = 'Sample value',
    datetime = 'Sample date'
  ) {
    this.id = id
    this.device_name = device_name
    this.value = value
    this.datetime = datetime
  }
}

export default event
