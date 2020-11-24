tag ?= latest
build:
	docker build . -t akdemo:$(tag)

static:
	docker-compose run --rm web python manage.py collectstatic

init:
	docker-compose up -d
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py collectstatic
	docker-compose exec web psql -h umami-db -U umami -d umami -f umami-schema.psql
	docker-compose ps

down:
	docker-compose down

clean:
	@make down
	docker volume rm umami-db akdemo-db akdemo-assets
