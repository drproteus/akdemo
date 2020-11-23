tag ?= latest
build:
	docker build . -t akdemo:$(tag)

static:
	docker-compose run --rm web python manage.py collectstatic
