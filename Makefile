.PHONY: build run 

build:
	docker build -t app .
run:
	docker run -p 70:80 app

