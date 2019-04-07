COMPOSE_DEV_FILE=docker-compose.yml


bootstrap-environment:
	poetry install
	$(RM) -rf athena.egg-info pip-wheel-metadata


reformat:
	poetry run isort -rc .
	poetry run black .

makemigrations:
	poetry run python manage.py makemigrations

.PHONY: migate
migrate:
	poetry run python manage.py migrate

tests:
	poetry run pytest

.PHONY: startapp
startapp: reformat migrate
	poetry run python manage.py runserver

.PHONY: startdb
startdb:
	docker-compose -f $(COMPOSE_DEV_FILE) up -d db

.PHONY: dbip
dbip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' athena_pgdb

.PHONY: compose-up
compose-up:
	docker-compose -f $(COMPOSE_DEV_FILE) up -d

compose-up-rebuild: docker-dev
	docker-compose -f $(COMPOSE_DEV_FILE) up -d

.PHONY: compose-logs
compose-logs:
	docker-compose -f $(COMPOSE_DEV_FILE) logs

.PHONY: compose-stop
compose-stop:
	docker-compose -f $(COMPOSE_DEV_FILE) stop

.PHONE: compose-athena-connect
compose-athena-connect:
	docker-compose -f $(COMPOSE_DEV_FILE) exec web /bin/bash

docker-dev: reformat
	docker build -t ippolab/athena-backend:dev .

docker-master: reformat
	docker build -t ippolab/athena-backend .

clean:
	$(RM) -rf *.egg-info
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs $(RM) -rf
