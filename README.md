# SbD_HealthApp <!-- omit in toc -->
Repo für die Laboraufgabe in Security by Design

## Table of Contents <!-- omit in toc -->
- [Starting App in Development Mode](#starting-app-in-development-mode)
	- [Create .env.dev file](#create-envdev-file)
	- [Build and start Docker Container](#build-and-start-docker-container)
	- [Create Superuser](#create-superuser)
	- [Create Groups](#create-groups)
	- [Use App](#use-app)
- [Starting App in Production Mode](#starting-app-in-production-mode)


## Starting App in Development Mode
Before starting the app in development mode, make sure you have installed Docker and Docker Compose on your machine. If you haven't, you can find the installation instructions [here](https://docs.docker.com/compose/install/).

### Create .env.dev file
Create a file called `.env.dev` in the root directory of the project. The file should contain the following environment variables:

```bash
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=hello_django_dev
SQL_USER=hello_django
SQL_PASSWORD=hello_django
SQL_HOST=db
SQL_PORT=5432
DATABASE=postgres
```
### Build and start Docker Container
Open terminal in root directory of the project and run the following command:
```bash
docker-compose up --build
```
### Create Superuser
Open terminal on running `web` docker container and run the following command:
```bash
python manage.py createsuperuser
```
### Create Groups
Open browser and navigate to `http://localhost:8000/admin/`. Login with the created superuser. Create the following groups:
- `patient`
- `doctor`

### Use App
Open browser and navigate to `http://localhost:8000/`. Create a new user and activate the user's eamil address. Login with the created patient and create a health record. 

## Starting App in Production Mode
