# Simple Climate App

## Getting Started
This is a simple app that displays temperature data of a given location using the OpenWeatherMap JSON API <http://openweathermap.org/forecast5>. The API requires an access token in the `GET` request using parameter `APPID`.


Before starting, you will need:

- Python 3.5 above
you can download here : https://www.python.org/downloads/
set pip and PATH to environment variables when installation


## Run the program

This is a simple app that displays temperature data of a given location using the OpenWeatherMap JSON API <http://openweathermap.org/forecast5>. The API requires an access token in the `GET` request using parameter `APPID`.

The app will consist of:

- A location picker with a list of cities.
- An index page that displays the daily temperature, daily variance, 5-day average.

### How to run the program :

- Use "run.bat" or follow steps below :

- Go to directory file you have cloned or downloaded, then open cmd in same directory

For example using `Windows + R` : "C:\Users\brian.estadimas\Downloads\climateApp\cmd"

- First we need to create environment variables (env) and active it :

`python -m venv env`

`env\Scripts\activate.bat`

- Then install requirement in env :

`pip install -r requirements.txt`

### Running test and server by using :

`python manage.py test`

`python manage.py runserver 8000`

- Open browser and type :

## http://localhost:8000/

### Source Code

To open source code you need sublime or notepad++

List of main files :

  - climateApp
    - climate
      - admin.py
      - apps.py (register app)
      - urls.py (setting url for app and other url rendered in views.py)
      - models.py (database, if necessary)
      - tests.py  (unit testing for implementation code)
      - views.py (main source code, stored procedure and function)
      - templates
        - index.html (HTML/CSS/Javascript code as template)
     - climateApp
        - urls.py (URL setting for all apps)
        - settings.py (Django settings)
     - manage.py (for testing and runserver)
  

#### Test and run server

![alt text](https://imgur.com/a/gYYoE9E)

![alt text](https://imgur.com/a/Km0IzQx)

