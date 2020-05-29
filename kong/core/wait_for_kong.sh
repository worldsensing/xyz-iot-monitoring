#!/usr/bin/env sh

# Condition will be 1 until Kong answers correctly, then will assume that it has been started ok
condition=1
while [ "$condition" -ne 0 ]
do
  echo "Waiting KONG to start"
  sleep 15
  curl -I http://localhost:8001/routes/ | grep -q "HTTP/1.1 200 OK"
  condition=$?
done
echo "KONG started"