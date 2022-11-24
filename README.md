# SbD_HealthApp <!-- omit in toc -->
Repo für die Laboraufgabe in Security by Design

## Table of Contents <!-- omit in toc -->
- [Starting App in Development Mode](#starting-app-in-development-mode)
	- [Build and start Docker Container](#build-and-start-docker-container)
	- [Create Superuser](#create-superuser)
	- [Create Groups](#create-groups)
	- [Use App](#use-app)
- [Starting App in Production Mode](#starting-app-in-production-mode)


## Starting App in Development Mode
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
