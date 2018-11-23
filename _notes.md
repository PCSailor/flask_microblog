# Setup of a Flask Microblog
### from Flask Mega-Tutorial by M. Grinberg
# Path:
* __init.py__
* routes.py
* microblog.py
    * Path soFar:
        * mircoblog
        *   venv/
        *       app/
        *           __init.py__
        *               routes.py
        * microblog.py
* index.html
* 
* 
* 
* 

# Log:
1. app.db changed to app_db.db & back to app.db
# Abbreviations
* virEnv = virtual environment
* envVar = environmental variable
## Commands
### The restart the App server:
1. Terminal into app folder
2. venv\Scripts\activate (Start virEnv)
3. FLASK_APP=microblog.py (sumName.py)
4. flask run
5. In browser, navigate to server, 127.0.0.1 or localhost:5000
# 
### All Commands
* pip install --upgrade pip
* pip install flask
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
    * 'set' or 'export'
* flask run
    * server running 127.0.0.1:5000/ or localhost:5000/  and ../index
* pip install python-dotenv
    * Register envVar in Flask that are auto-imported with flask command run
* pip install flask-wtf
    * 1st flask extension added
    * wrapper around the WTForms package
* pip install flask-sqlalchemy
* pip install flask-migrate
* flask db init
* flask db migrate -m "messagesGoesHere"
* flask db upgrade
* flask shell
    * python interrupter run in the context of an application
* 