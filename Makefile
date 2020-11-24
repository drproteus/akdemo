tag ?= latest
build:
	docker build . -t akdemo:$(tag)

migrate:
	@echo --- Running Migrations
	docker-compose exec web python manage.py migrate

static:
	@echo --- Collecting Static Assets
	docker-compose exec web python manage.py collectstatic

loaddata:
	@echo --- Loading Fixture Data
	docker-compose exec web python manage.py loaddata public/fixtures/resources.json

loadumami:
	@echo --- Loading Analytics Schema
	docker-compose run --rm -v `pwd`:/data -e PGPASSWORD=umami \
				umami-db psql -h umami-db \
				-U umami -d umami -f /data/umami-schema.psql

defaultadmin:
	@echo --- Creating Superuser account admin [admin@akdemo.ngrok.io]
	docker-compose exec web python manage.py createsuperuser --username admin@akdemo.ngrok.io --email admin@akdemo.ngrok.io

init:
	docker-compose up -d
	@make static
	@echo --- Waiting for DBs... && sleep 5
	@make migrate
	@make loaddata
	@make loadumami
	docker-compose restart
	@make defaultadmin
	docker-compose ps

down:
	docker-compose down

clean:
	@make down
	docker volume rm akdemo_umami-db akdemo_akdemo-db akdemo_akdemo-assets

ngrok:
	ngrok start -authtoken "$(NGROK_AUTH_TOKEN)" --config ngrok.yml --all
