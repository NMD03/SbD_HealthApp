# SbD_HealthApp <!-- omit in toc -->
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

Repository for the SbD Health App

## Table of Contents <!-- omit in toc -->
- [Documentation](#documentation)
- [Starting App in Development Mode](#starting-app-in-development-mode)
	- [Create .env.dev file](#create-envdev-file)
	- [Build and start Docker Container](#build-and-start-docker-container)
	- [Create Superuser](#create-superuser)
	- [Create Groups](#create-groups)
	- [Use App](#use-app)
	- [Stop Docker Container](#stop-docker-container)
- [Starting App in Production Mode](#starting-app-in-production-mode)
	- [Create .env Files](#create-env-files)
	- [Build and Start Docker Container](#build-and-start-docker-container-1)
	- [Migrate Database](#migrate-database)
	- [Collect Static Files](#collect-static-files)
	- [Create Superuser](#create-superuser-1)
	- [Create Groups](#create-groups-1)
	- [Use App](#use-app-1)
	- [Stop Docker Container](#stop-docker-container-1)


## Documentation
You can find the full documentation required for the project submission [here](./Documentation.md)

## Starting App in Development Mode
Before starting the app in development mode, make sure you have installed Docker and Docker Compose on your machine. If you haven't, you can find the installation instructions [here](https://docs.docker.com/compose/install/).

### Create .env.dev file
Create a file called `.env.dev` in the root directory of the project. The file should contain the following environment variables:

```bash
SECRET_KEY= # your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE= # your database name
SQL_USER= # your database user
SQL_PASSWORD= # your database password
SQL_HOST= # your database host
SQL_PORT= # your database port
DATABASE= # your database 
```
### Build and start Docker Container
Open terminal in root directory of the project and run the following command:
```bash
docker-compose up --build
```
### Create Superuser
Open terminal in root directory of the project and run the following command:
```bash
docker-compose exec web python manage.py createsuperuser
```
Type in a username and password for the superuser.
### Create Groups
Open browser and navigate to `http://localhost:8000/admin/`. Login with the created superuser. Create the following groups:
- `patient`
- `doctor`

### Use App
Open browser and navigate to `http://localhost:8000/`. Create a new user and activate the user's eamil address. Login with the created patient and create a health record. 

### Stop Docker Container
Open terminal in root directory of the project and run the following command:
```bash
docker-compose down -v
```

## Starting App in Production Mode
Before starting the app in production mode, make sure you have installed Docker and Docker Compose on your machine. If you haven't, you can find the installation instructions [here](https://docs.docker.com/compose/install/).

### Create .env Files
Create a file called `.env.prod` in the root directory of the project. The file should contain the following environment variables:

```bash
DEBUG=0
SECRET_KEY= # your secret key
DJANGO_ALLOWED_HOSTS= # your allowed hosts
SQL_ENGINE= # your sql engine
SQL_DATABASE= # your sql database name
SQL_USER= # your sql user
SQL_PASSWORD= # your sql password
SQL_HOST= # your sql host
SQL_PORT= # your sql port
DATABASE= # your database
```
Create a file called `.env.prod.db` in the root directory of the project. The file should contain the following environment variables:

```bash
POSTGRES_DB= # your postgres db
POSTGRES_USER= # your postgres user
POSTGRES_PASSWORD= # your postgres password
```
### Build and Start Docker Container
Open terminal in root directory of the project and run the following command:
```bash
docker-compose -f docker-compose.prod.yml up --build
```
### Migrate Database
Open terminal in root directory of the project and run the following command:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
```
### Collect Static Files
Open terminal in root directory of the project and run the following command:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

### Create Superuser
Open terminal in root directory of the project and run the following command:
```bash
docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser
```
Type in a username and password for the superuser.
### Create Groups
Open browser and navigate to `http://localhost:8000/admin/`. Login with the created superuser. Create the following groups:
- `patient`
- `doctor`

### Use App
Open browser and navigate to `http://localhost:8000/`. Create a new user and activate the user's eamil address. Login with the created patient and create a health record.

### Stop Docker Container
Open terminal in root directory of the project and run the following command:
```bash
docker-compose -f docker-compose.prod.yml down -v
```
