# Makefile
.PHONY: migrations migrate superuser run

migrations:
    docker-compose run web-app python manage.py makemigrations

migrate:
    docker-compose run web-app python manage.py migrate

# superuser:
#     docker-compose exec web-app python manage.py createsuperuser

run:
    docker-compose up
