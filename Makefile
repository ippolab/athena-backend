COMPOSE_DEV_FILE=docker-compose-dev.yml


bootstrap-environment:
	mkvirtualenv athena-backend && pip install poetry && poetry install

.PHONY: activate-environment
activate-environment:
	workon athena-backend

collectstatic:
	python manage.py collectstatic --noinput

.PHONY: startapp
startapp:
	python manage.py runserver

.PHONY: startdb
startdb:
	docker-compose -f $(COMPOSE_DEV_FILE) up db

.PHONE: dbip
dbip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' athena_pgdb

compose-up: collectstatic
	docker-compose -f $(COMPOSE_DEV_FILE) up -d

compose-up-rebuild: docker-dev
	docker-compose -f $(COMPOSE_DEV_FILE) up -d

compose-logs: collectstatic
	docker-compose -f $(COMPOSE_DEV_FILE) logs

.PHONY: compose-stop
compose-stop:
	docker-compose -f $(COMPOSE_DEV_FILE) stop

.PHONE: compose-athena-connect
compose-athena-connect:
	docker-compose -f $(COMPOSE_DEV_FILE) exec web /bin/bash

docker-dev:
	docker build -t ippolab/athena-backend:dev .

docker-master:
	docker build -t ippolab/athena-backend .
