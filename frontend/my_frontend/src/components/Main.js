import React, { Component } from 'react'
import { Redirect, Route, Switch } from 'react-router-dom'
import DeviceTab from '../views/device.js'
import EventTab from '../views/event.js'
import BusinessRuleTab from '../views/businessRule.js'
import GrafanaTab from '../views/grafana.js'
import NodeRedTab from '../views/nodered.js'

import '../App.css'

class Main extends Component {
  render() {
    return (
      <div className="app-content">
        <Switch>
          <Route path="/event" component={EventTab} />
          <Route path="/device" component={DeviceTab} />
          <Route path="/business-rule" component={BusinessRuleTab} />
          <Route path="/grafana" component={GrafanaTab} />
          <Route path="/nodered" component={NodeRedTab} />
          <Redirect from="/" to="/event" />
        </Switch>
      </div>
    )
  }
}

export default Main
