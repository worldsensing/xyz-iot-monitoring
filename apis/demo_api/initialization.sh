# Initialize the demo_api project
docker-compose -f docker-compose.yml up -d postgres
sh ./scripts/configure_postgres.sh demo_api_postgres_1 api_db
docker-compose -f docker-compose.yml stop

docker-compose -f docker-compose.unittest.yml -p unittests up -d postgres
sh ./scripts/configure_postgres.sh unittests_postgres_1 api_db_test
docker-compose -f docker-compose.unittest.yml -p unittests stop