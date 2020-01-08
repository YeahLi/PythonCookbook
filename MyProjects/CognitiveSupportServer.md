# Cognitive Support Server
## Introduction
Developed a cognitive server to improve technical support's daily work. The project is using Python Flask framework and Spark technologies. It was deployed on IBM Cloud. 
Highlight Features:
1. Monitor tickets pool and send notifications to technical engineer if there's new ticket coming.
==> Minimized the delay of initial reply and improved client's satisfaction.
2. Analyze and predict customer's satisfaction. Send alerts to management and engineers to help avoid potential escalations. Send alerts to support engineer if the ticket is from tough customers.
==> Helped management to distribute resources more efficiently and minimize the business influence caused by product issues.

## Architecture
1. Salesforce tickets
2. User managment
3. Set New Update Frequency
4. logs

## Techniques
1. Frontend: Server Admin Website
**index.html**
```
<!DOCTYPE html>
{% extends "base.html" %}
{% block content %}
    <table id="indexTable">
        <tr>
            <td style='width: 300px;'><img class = 'newappIcon' src='/static/images/login_image_175x175.png'>
            </td>
            <td>
                <h1 id = "message">Support Cognitive Server V1.0</h1>
                <p class='description'></p>Receiving PMR's information from collector and sending information to PMR notifier.
            </td>
        </tr>
    </table>
{% endblock %}
```

**base.html**
```
<!DOCTYPE html>
<html>
<head>
    {% if title %}
    <title>IBM Spectrum Cognitive RESTful Server - {{ title }}</title>
    {% else %}
    <title>IBM Spectrum Cognitive RESTful Server</title>
    {% endif %}
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="stylesheet" href="/static/stylesheets/style.css" />
</head>
<body>
    <table id="baseTable">
        <tr>
            <td>
                <a href="/index">Home</a>
            </td>
            <td>
                <a href="/SF">SalesForce</a>
            </td>
            <td>
                <a href="/configuration">Settings</a>
            </td>
            {% if user == "Admin" %}
            <td>
                <a href="/log">Server Log</a>
            </td>
            {% endif %}

            <td>{{ user }}</td>
        </tr>
    </table>
    {% block content %}{% endblock %}
</body>
</html>
```

2. Backend: REST API to handle multiple requests
```python
from flask import *
app = Flask(__name__)
# set application variable
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Implement a REST API
@app.route('/SF', methods=['GET', 'POST'])
@auth.login_required
def access_SF_info():
    serverlog.debug(request.headers)
    if request.method == 'POST':
        if update_from_SF(SF_DATA_FILE_NAME):
            serverlog.info("User <%s> uploaded file <%s> successfully.", auth.username(), SF_DATA_FILE_NAME)
            return 'Upload done.'
        else:
            serverlog.error("User <%s> uploaded file <%s> failed.", auth.username(), SF_DATA_FILE_NAME)
            abort(400)
    else:
        return send_from_directory(app.config['UPLOAD_FOLDER'], SF_DATA_FILE_NAME, cache_timeout=10,  mimetype='application/json')
# start server
if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    new_user('Admin', 'Admin')
    app.run(host='0.0.0.0', port=8080)
```

3. Database SQLLite:
```python
from flask_sqlalchemy import SQLAlchemy
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)
# Create DB object
db = SQLAlchemy(app)
if not os.path.exists('db.sqlite'):
    db.create_all()
# Define a Table called users
class User(db.Model):
    __tablename__ = 'users'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

    # Call pwd_context.encrypt to hash password when creating a user
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    # Call pwd_context.verify to check the input password with password in DB
    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    # Use itsdangerous to generate token
    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # vSalid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user
#
# query data
if User.query.filter_by(username=username).first() is not None:
    return False        # No change at this moment
# add record
user = User(username=username)
user.hash_password(password)
db.session.add(user)
db.session.commit()
# remove record
User.query.filter_by(username=username).delete()
db.session.commit()
```

4. Loggging:
```python
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pprint import pprint
#Configuration:
logging.Formatter.converter = time.gmtime
log_formatter = logging.Formatter('[%(asctime)s GMT] %(levelname)s %(funcName)s:(%(lineno)d) %(message)s')
serverlogFile = 'logs/server.log'
serverlog_handler = RotatingFileHandler(serverlogFile, mode='a', maxBytes=20*1024*1024, backupCount=2, encoding=None, delay=0)
serverlog_handler.setFormatter(log_formatter)
serverlog_handler.setLevel(logging.INFO)
serverlog = logging.getLogger('serverlog')
serverlog.addHandler(serverlog_handler)
# logging
serverlog.debug("Write debug logs")
serverlog.info("Write info logs")
serverlog.error("Write error logs")
```

5. Authentication
```python
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()
# Set token expire time
TOKEN_EXPIRED_TIME = 600 # seconds
# Authentication will be called by the framework to verify that the username and password combination provided by the client are valid. 
@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            serverlog.error("User <%s> logon failed. Wrong username or password.", auth.username())
            return False
    g.user = user
    serverlog.info("User <%s> logon successfully.", auth.username())
    return True
# add auth tag in rest api function
@app.route('/')
@app.route('/index')
@auth.login_required
def index():
    serverlog.debug("Request Headers: %s", request.headers)
    return render_template('index.html', user=auth.username())
```

6. JSON data handling
```python
#Handle JSON data from a json file.
def splitCasesByProduct():
    # Load the source data
    path = os.path.join(app.config['UPLOAD_FOLDER'], SF_DATA_FILE_NAME)
    with open(path, 'r') as f:
        data = json.load(f)
        #print(data)
    # Get source data collected time
    serverlog.info("Agent <%s> sent data at <%s>.", data['Agentname'], data['Updatetime'])
```
```python    
#Handle JSON data from REST API
import requests
import json
from pprint import pprint
#Get token from RESTful server
print "Fetching token..."
url = 'https://cognitivesupportserver.w3ibm.mybluemix.net/token'
response = requests.post(url, None, auth=('Admin', 'Admin'))
result = response.json()
token = result['token']
if token:
    print "Token: %s" % token
else:
    print "Get token failed."
# Use token to get info
print "Use token to fetch data...."
url = 'https://cognitivesupportserver.w3ibm.mybluemix.net/product/SpectrumConductorwithSpark?retain_id=048595'
response = requests.get(url, None, auth=(token, 'random'))
if response.content:
    #print "Response:\n %s" % response.content
    data = json.loads(response.content)
    pprint(data)
else:
    print "Get response failed from REST server for SF"
```