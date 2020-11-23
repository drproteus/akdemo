tag ?= latest
build:
	docker build . -t akdemo:$(tag)
