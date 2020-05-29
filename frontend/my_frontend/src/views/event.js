import React from 'react'
import Container from '@material-ui/core/Container'
import Paper from '@material-ui/core/Paper'

import EnhancedTable from '../components/table/EnhancedTable.js'
import DeviceAPI from '../api/deviceAPI.js'
import EventAPI from '../api/eventAPI.js'
import Device from '../models/device.js'
import Event from '../models/event.js'

function createData(id, device_name, value, datetime) {
  return { id, device_name, value, datetime }
}

export class EventTab extends React.Component {
  constructor(props) {
    super(props)

    this.randomIDToForceRefresh = 0
    this.state = {
      events: [],
      eventsRows: [],
      filterValues: ['All Devices']
    }
  }

  componentDidMount() {
    EventAPI.getAllEvents(false, (response) => {
      var eventsFromApi = response.message.map((event) => {
        return new Event(event.id, event.device_name, event.value, event.datetime)
      })
      var resultRows = eventsFromApi.map((event) => {
        return createData(event.id, event.device_name, event.value, event.datetime)
      })
      this.setState({ events: eventsFromApi, eventsRows: resultRows })
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
        id: 'device_name',
        label: 'Device'
      },
      {
        id: 'value',
        label: 'Value'
      },
      {
        id: 'datetime',
        label: 'Date'
      }
    ]

    this.randomIDToForceRefresh++
    return (
      <Container style={{ marginTop: '20px' }}>
        <Paper key={this.randomIDToForceRefresh}>
          <EnhancedTable
            toolbarTitle={'Events'}
            filterValues={this.state.filterValues}
            dataColumns={columns}
            dataRows={this.state.eventsRows}
          />
        </Paper>
      </Container>
    )
  }
}

export default EventTab
