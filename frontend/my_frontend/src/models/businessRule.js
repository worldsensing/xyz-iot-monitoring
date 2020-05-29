// Model of BusinessRule that match with the API's Model

class businessRule {
  constructor(id, name = 'Sample name', query = 'Sample query', executing = false) {
    this.id = id
    this.name = name
    this.query = query
    this.executing = executing
  }
}

export default businessRule
