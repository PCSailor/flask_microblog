# Setup of a Flask Microblog
### from Flask Mega-Tutorial by M. Grinberg
## Abbreviations
* virEnv = virtual environment
* envVar = environmental variable
## Commands
### To reestablish a connection & return to work
* From terminal, navigate to apps root folder
    * source venv/scripts/activate
    * FLASK_APP=sumName.py
    * flask run
* From browser, navigate to http://127.0.0.1:5000/ or http://localhost:5000/
### All Commands
* python -m venv venv
    * creates virEnv
* source venv/scripts/activate
    * activates virEnv
    * could be venv/bin/activate
* python -m pip install --upgrade pip
    * upgrade pip
* pip install flask
    * virEnv of Flask
* set FLASK_APP=microblog.py (from root dir)
    * how to import the app by setting the Flask app envir variable
* flask run
    * server is running (http://127.0.0.1:5000/)
* http://localhost:5000/ (in browser)
    * also http://localhost:5000/index
* pip install python-dotenv
    * Register envVar in Flask that are auto-imported with flask command run
* pip install flask-wtf
    * 1st flask extension added
    * wrapper around the WTForms package