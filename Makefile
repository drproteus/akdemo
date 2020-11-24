tag ?= latest
build:
	docker build . -t akdemo:$(tag)

static:
	docker-compose run --rm web python manage.py collectstatic

init:
	docker-compose up -d
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py collectstatic
	docker-compose exec web python manage.py loaddata public/fixtures/resources.json
	docker-compose exec web psql -h umami-db -U umami -d umami -f umami-schema.psql
	docker-compose restart
	docker-compose ps

down:
	docker-compose down

clean:
	@make down
	docker volume rm akdemo_umami-db akdemo_akdemo-db akdemo_akdemo-assets

ngrok:
	ngrok start -authtoken "$(NGROK_AUTH_TOKEN)" --config ngrok.yml --all
