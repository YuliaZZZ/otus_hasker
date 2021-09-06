start:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

activate:
	source ./venv/bin/activate

install:
	pip3 install -r requirements.txt

docker-build:
	DOCKER_BUILDKIT=1 docker image build -t hasker .

docker-start:
	docker-compose up

test:
	python3 manage.py test

shell:
	python3 manage.py shell

user:
	python3 manage.py createsuperuser

static:
	python3 manage.py collectstatic






.PHONY : start migrate activate install docker-start sort black test shell static