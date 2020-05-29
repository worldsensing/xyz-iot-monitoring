import React from 'react'
import Iframe from 'react-iframe'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'

import config from '../config'
import EnhancedTable from '../components/table/EnhancedTable.js'
import DeviceAPI from '../api/deviceAPI.js'
import DeviceCategoryAPI from '../api/deviceCategoryAPI.js'
import Device from '../models/device.js'
import DeviceCategory from '../models/deviceCategory.js'

function createData(name, category, location) {
  return { name, category, location }
}

export class DeviceTab extends React.Component {
  constructor(props) {
    super(props)

    this.randomIDToForceRefresh = 0
    this.state = {
      selectedDeviceName: '',
      devices: [],
      devicesRows: [],
      filterValues: []
    }
  }

  componentDidMount() {
    DeviceCategoryAPI.getAllDeviceCategories(false, (response) => {
      var devicesCategoriesFromApi = response.message.map((deviceCategory) => {
        return new DeviceCategory(deviceCategory.name, deviceCategory.data_type)
      })

      DeviceAPI.getAllDevices(false, (response) => {
        var devicesFromApi = response.message.map((device) => {
          return new Device(device.name, device.category, device.location)
        })
        var resultRows = devicesFromApi.map((device) => {
          var extraCategoryInfo = ''
          for (var i = 0; i < devicesCategoriesFromApi.length; ++i) {
            if (devicesCategoriesFromApi[i].name === device.category) {
              extraCategoryInfo = devicesCategoriesFromApi[i].data_type
              break
            }
          }
          return createData(
            device.name,
            `${device.category} (${extraCategoryInfo})`,
            device.location
          )
        })
        this.setState({ devices: devicesFromApi, devicesRows: resultRows })

        if (resultRows.length > 0) {
          this.onClickonRow(resultRows[0])
        }
      })

      console.log(devicesCategoriesFromApi)
    })
  }

  onClickonRow(row) {
    this.setState({ selectedDeviceName: row.name })
  }

  render() {
    const columns = [
      {
        id: 'name',
        label: 'Name'
      },
      {
        id: 'category',
        label: 'Category'
      },
      {
        id: 'location',
        label: 'Location'
      }
    ]

    this.randomIDToForceRefresh++

    return (
      <Grid
        container
        spacing={2}
        justify="center"
        alignItems="flex-start"
        style={{ marginTop: '20px' }}
      >
        <Grid item xs={5}>
          <Paper key={this.randomIDToForceRefresh}>
            <EnhancedTable
              toolbarTitle={'Devices'}
              filterValues={this.state.filterValues}
              dataColumns={columns}
              dataRows={this.state.devicesRows}
              onClickonRow={this.onClickonRow.bind(this)}
            />
          </Paper>
        </Grid>
        <Grid item xs={5}>
          <Paper key={this.randomIDToForceRefresh} style={{ height: '375px' }}>
            <Iframe
              url={`${config.services.grafana.url}/d/VyeKOtuZl/device-dashboard?orgId=1&var-device_name=${this.state.selectedDeviceName}&kiosk&fullscreen`}
              width="100%"
              height="100%"
            />
          </Paper>
        </Grid>
      </Grid>
    )
  }
}

export default DeviceTab
