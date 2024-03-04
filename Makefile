.PHONY: download

download:
	python3 manage.py loaddata fixtures/article_fixtures.json
	python3 manage.py loaddata fixtures/main_fixtures.json
	python3 manage.py loaddata fixtures/servises_fixtures.json
	python3 manage.py loaddata fixtures/users_fixtures.json


docker_build:
	docker-compose build

docker_server:
	docker-compose up -d

down_all:
	docker-compose down

docker_migrate:
	docker-compose exec django python manage.py migrate --noinput

docker_createsuperuser:
	docker-compose exec django python manage.py createsuperuser
