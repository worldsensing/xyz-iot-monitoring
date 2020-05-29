import React from 'react'
import Iframe from 'react-iframe'

import config from '../config'

export class NodeRedTab extends React.Component {
  constructor(props) {
    super(props)

    this.state = {}
  }

  componentDidMount() {}

  render() {
    return <Iframe url={`${config.services.nodered.url}`} width="100%" height="100%" />
  }
}

export default NodeRedTab
