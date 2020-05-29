NAME=demo_api
DOCKER_NAME=phd/$(NAME)
VERSION=1.0.0-RC1
DOCKER_NAME_FULL=$(DOCKER_NAME):$(VERSION)
DOCKER_LOCALHOST=$(shell ip addr show docker0 | grep -Po 'inet \K[\d.]+')
DOCKER_VOLUME_REPORTS=$(shell pwd)/reports

clean:
	@find . -iname "*~" | xargs rm 2>/dev/null || true
	@find . -iname "*.pyc" | xargs rm 2>/dev/null || true
	@find . -iname "build" | xargs rm -rf 2>/dev/null || true

build: clean
	docker build -t $(DOCKER_NAME_FULL) .

run: build
	docker run -it -p 5001:5000 \
	    --add-host postgres:$(DOCKER_LOCALHOST) \
	    --network demo_api_private \
	    --name $(NAME) \
	    --env-file ENV/api.env \
	    --rm $(DOCKER_NAME_FULL)

run-unittests: build
	docker run -i --name $(NAME) \
		-v $(DOCKER_VOLUME_REPORTS):/opt/$(NAME)/reports \
		--add-host postgres:$(DOCKER_LOCALHOST) \
		--network unittests_unittests \
		--env-file ENV/test.env --rm $(DOCKER_NAME_FULL) "/opt/api/scripts/run_tests.sh"

setup:
	docker-compose -f docker-compose.yml up -d

setup-unittests:
	docker-compose -f docker-compose.unittest.yml -p unittests up -d