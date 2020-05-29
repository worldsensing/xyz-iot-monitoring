PhD Deployment
===================

# Grafana

### Entry
```SQL
SELECT TO_TIMESTAMP(date, 'YYYY/MM/DD HH24:MI:SS') as "time", value
 FROM entry 
 WHERE entry.device_name = 'ABC-1001'
```

`http://localhost:3001/d/VyeKOtuZl/device-dashboard?orgId=1&var-device_name=ABC-1002`
### Device
