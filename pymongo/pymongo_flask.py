from flask import Flask
from flask.ext.pymongo import PyMongo

@app.route('/')
def home_page():
    online_users = mongo.db.users.find({'online': True})
    return render_template('index.html',
        online_users=online_users)

app = Flask(__name__)
mongo = PyMongo(app)