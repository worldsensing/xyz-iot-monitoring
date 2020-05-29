# Register Frontend
sh ./core/manage.sh "frontend" "http://frontend_demo:80" "frontend-route-a" "/"

# Register Grafana
sh ./core/manage.sh "grafana-frontend" "http://grafana:3000" "grafana-frontend-route-a" "/grafana"

# Register Nodered
sh ./core/manage.sh "nodered-frontend" "http://node-red:1880" "nodered-frontend-route-a" "/nodered"

# Register Backend APIs
## Device Category
sh ./core/manage.sh "api-device-category" "http://backend_demo_api:5000/device-categories" "api-device-category-route-a" "/api/device-categories"
## Data Types
sh ./core/manage.sh "api-data-type" "http://backend_demo_api:5000/data-types" "api-data-type-route-a" "/api/data-types"
## Device
sh ./core/manage.sh "api-device" "http://backend_demo_api:5000/devices" "api-device-route-a" "/api/devices"
## Event
sh ./core/manage.sh "api-event" "http://backend_demo_api:5000/events" "api-event-route-a" "/api/events"
## Business Rule
sh ./core/manage.sh "api-business-rule" "http://backend_demo_api:5000/business-rules" "api-business-rule-route-a" "/api/business-rules"
## Location
sh ./core/manage.sh "api-location" "http://backend_demo_api:5000/locations" "api-locations-route-a" "/api/locations"

# Examples
#curl -i -X POST --url http://localhost:8001/services/ --data 'name=example-service' --data 'url=http://mockbin.org'
#curl -i -X POST --url http://localhost:8001/services/example-service/routes --data 'name=route-name' --data 'paths[]=/foo&paths[]=/bar'

## Delete
#curl -X DELETE --url http://localhost:8001/services/{service name or id}
#curl -X DELETE --url http://localhost:8001/services/{service name or id}/routes/{route name or id}
