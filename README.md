# SbD_HealthApp <!-- omit in toc -->
Repo für die Laboraufgabe in Security by Design

## Table of Contents <!-- omit in toc -->
- [Prerequisites](#prerequisites)
	- [Python Environment](#python-environment)


## Prerequisites
### Python Environment
We used `Python 3.10.0` for our project. So make sure you have the right python version installed:
```
python --version
```
if the right version is installed you can create the python virtual environment. For that head into the Project directory and run the following commands:
1. **Create the environment:**<br>
	On Windows:
	```
	py -m venv env
	```
2. **Activate the environment**<br>
	On Windows:
	```
	env\Scripts\activate.bat
	```
	On Unix or MacOS:
	```
	source env/bin/activate
	```
	After successfully activating the environment your command prompt should display `(env)` in front of your path.
3. **Install the required packages using `requirements.txt`**<br>
	After activating the environment you can install all the python packages needed with the following command
	```
	py -m pip install -r requirements.txt
    ```

## Starting App locally
1. **Activate the environment**<br>
	On Windows:
	```
	env\Scripts\activate.bat
	```
	On Unix or MacOS:
	```
	source env/bin/activate
	```
	After successfully activating the environment your command prompt should display `(env)` in front of your path.
2. **Start the app**<br>
	After activating the environment you can start the app. For that you have to navigate int the `health_app` directory:
	```
	cd health_app
	```
	After that you can start the app with the following command:
	```
	python manage.py runserver
	```
	After that you can access the app on `http://localhost:8000/`

