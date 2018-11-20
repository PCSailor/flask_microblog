'''
pg 7
'''
from app import app
# a decorator modifies the function that follows it
@app.route('/') # decorator
@app.route('/index') # decorator
def index():
    # return 'Hello World'
    # pg12 Ch 2_Templates
    user = {'username': 'Phil'}
    return '''
    <html>
        <head>
            <title>Phil Curtis' Tech Blog</title>
        <head>
        <body>
            <h1>Hello ''' + user['username'] + '''!</h1>
        </body>
    </html>'''

