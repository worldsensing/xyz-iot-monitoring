XYZ: IoT Monitoring of Infrastructures using Microservices
===================

Main repository for the _XYZ: IoT Monitoring of Infrastructures using Microservices_ project.

This repository is the codebase for the paper:

> M. Vila, M.-R. Sancho, E. Teniente, XYZ Monitor: IoT Monitoring of Infrastructures using Microservices, in: International Conference on Service-Oriented Computing (ICSOC) STRAPS Workshop, 2021, pp. 472–484. https://link.springer.com/chapter/10.1007%2F978-3-030-76352-7_43

Main purpose of our system: to monitor IoT devices so that it can automatically react and notify when a given alarm is detected. Handle alarms that are defined by means of business rules and allow setting ontological requirements over the information handled.

_(Section under construction)_

![Devices frontend with Grafana](https://github.com/worldsensing/xyz-iot-monitoring/blob/master/extra/frontend_devices_mod.png?raw=true)

## Architecture
Microservices based, with Docker and Docker compose.

```
.
├── apis
│   └── demo_api
├── frontend
│   ├── grafana
│   ├── my_frontend (react)
│   └── nginx
├── kong
├── nodered
└── README.md
```

## Requirements
The project has been tested under Ubuntu.
- docker
- docker-compose

## Installation
- Run `./initialization.sh`
- Follow the steps on `./nodered/README.md`, `set-up` section

## Running the project
- Run `./start.sh`

### Stop
- Run `./stop.sh`

## Troubleshooting
