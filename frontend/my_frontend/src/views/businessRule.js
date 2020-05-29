import React from 'react'
import Container from '@material-ui/core/Container'
import Paper from '@material-ui/core/Paper'

import EnhancedTable from '../components/table/EnhancedTable.js'
import BusinessRuleAPI from '../api/businessRuleAPI.js'
import DeviceAPI from '../api/deviceAPI.js'
import BusinessRule from '../models/businessRule.js'
import Device from '../models/device.js'

function createData(id, name, query, executing) {
  executing = executing ? 'Yes' : 'No'

  return { id, name, query, executing }
}

export class BusinessRuleTab extends React.Component {
  constructor(props) {
    super(props)

    this.randomIDToForceRefresh = 0
    this.state = {
      businessRules: [],
      businessRulesRows: [],
      filterValues: ['All Devices']
    }
  }

  componentDidMount() {
    BusinessRuleAPI.getAllBusinessRules(false, (response) => {
      var businessRulesFromApi = response.message.map((business_rule) => {
        return new BusinessRule(
          business_rule.id,
          business_rule.name,
          business_rule.query,
          business_rule.executing
        )
      })
      var resultRows = businessRulesFromApi.map((business_rule) => {
        return createData(
          business_rule.id,
          business_rule.name,
          business_rule.query,
          business_rule.executing
        )
      })
      this.setState({ businessRules: businessRulesFromApi, businessRulesRows: resultRows })
    })

    DeviceAPI.getAllDevices(false, (response) => {
      var devicesFromApi = response.message.map((device) => {
        return new Device(device.name, device.category, device.location)
      })
      var resultFilters = devicesFromApi.map((device) => {
        return device.name
      })
      resultFilters.unshift('All Devices')
      this.setState({ filterValues: resultFilters })
    })
  }

  render() {
    const columns = [
      {
        id: 'id',
        label: 'ID'
      },
      {
        id: 'name',
        label: 'Name'
      },
      {
        id: 'query',
        label: 'Query'
      },
      {
        id: 'executing',
        label: 'Executing'
      }
    ]

    this.randomIDToForceRefresh++
    return (
      <Container style={{ marginTop: '20px' }}>
        <Paper key={this.randomIDToForceRefresh}>
          <EnhancedTable
            toolbarTitle={'Business Rules'}
            filterValues={this.state.filterValues}
            dataColumns={columns}
            dataRows={this.state.businessRulesRows}
          />
        </Paper>
      </Container>
    )
  }
}

export default BusinessRuleTab
