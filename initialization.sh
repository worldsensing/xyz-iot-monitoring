# Initialize the demo_api project
docker-compose up -d postgres
sh ./apis/demo_api/scripts/configure_postgres.sh phd_deployment_postgres_1 api_db