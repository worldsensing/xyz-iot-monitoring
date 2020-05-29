import React, { Component } from 'react'
import { NavLink } from 'react-router-dom'

import '../App.css'

class Header extends Component {
  render() {
    return (
      <div>
        <header className="header">
          <div>
            <ul className="navbar-nav">
              <li className="nav-item">
                <NavLink className="nav-link" to="/event" activeStyle={{ fontWeight: '600' }}>
                  Events
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/device" activeStyle={{ fontWeight: '600' }}>
                  Devices
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink
                  className="nav-link"
                  to="/business-rule"
                  activeStyle={{ fontWeight: '600' }}
                >
                  Business Rules
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/grafana" activeStyle={{ fontWeight: '600' }}>
                  Grafana Monitoring
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/nodered" activeStyle={{ fontWeight: '600' }}>
                  Nodered Business Rules
                </NavLink>
              </li>
            </ul>
          </div>
        </header>
      </div>
    )
  }
}

export default Header
