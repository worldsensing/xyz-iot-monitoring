# Script just for testing and debugging purposes
docker-compose -f docker-compose.unittest.yml -p unittests stop
sudo rm -rf /var/opt/api_test/pg_data
sh initialization.sh