#!/usr/bin/env bash

usage() {
  echo "usage: bash start.sh [ --rebuild_kong [yes/NO] --rebuild_docker [yes/NO] --rebuild_frontend [yes/NO] --rebuild_postgres [yes/NO] ]
  The script will start the docker containers and configure the Kong endpoints

  To rebuild all:
  bash start.sh --rebuild_kong yes --rebuild_docker yes --rebuild_frontend yes --rebuild_postgres yes

  To rebuild all without modifying the API DB:
  bash start.sh --rebuild_kong yes --rebuild_docker yes --rebuild_frontend yes
  "
}

rebuild_kong="no"
rebuild_docker="no"
rebuild_frontend="no"
rebuild_postgres="no"
while [ "$1" != "" ]; do
  case $1 in
  --rebuild_kong)
    shift
    rebuild_kong=$1
    ;;
  --rebuild_docker)
    shift
    rebuild_docker=$1
    ;;
  --rebuild_frontend)
    shift
    rebuild_frontend=$1
    ;;
  --rebuild_postgres)
    shift
    rebuild_postgres=$1
    ;;
  --help)
    usage
    exit
    ;;
  *)
    usage
    exit 1
    ;;
  esac
  shift
done

if [ ! "$BASH_VERSION" ]; then
  echo "Please do not use sh to run this script, execute it with bash" 1>&2
  exit 1
fi

if [ "$rebuild_postgres" == "yes" ]; then
  echo "Postgres - Delete API database and initialize"
  docker-compose stop postgres
  sudo rm -rf /var/opt/api/pg_data
  sh initialization.sh
fi

if [ ! -d ./frontend/my_frontend/build ] || [ "$rebuild_frontend" == "yes" ]; then
  echo "Frontend - Building process started"
  cd ./frontend/my_frontend/ || exit

  echo "Frontend - Clean old information"
  rm -rf ./build || true
  rm -rf ./node_modules || true

  echo "Frontend - Build new frontend"
  npm install && npm run build

  echo "Frontend - Deploying to nginx"
  cd ./../nginx/ && ./setup.sh
  cd ../../
fi

if [ "$rebuild_docker" == "yes" ]; then
  echo "DEPLOY - Rebuilding and pulling docker images"
  docker-compose build
  docker-compose pull
fi

echo "DEPLOY - Starting services"
docker-compose up -d
cd kong || exit
sh ./core/wait_for_kong.sh

if [ "$rebuild_kong" == "yes" ]; then
  echo "KONG - Configuring endpoints"
  sh ./endpoints.sh
fi
