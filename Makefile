run:
	python src/main.py
build:
	docker build -t "test_nginx_1" .
up:
	docker-compose up --build --scale web=2
down:
	docker-compose down
