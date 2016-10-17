# To build

1. docker volume create --name=data
2. docker-compose up --build
3. docker-compose run web python manage.py collectstatic --noinput
4. docker-compose run web python manage.py migrate
5. docker-compose run web python manage.py createsuperuser
6. docker-compose up
