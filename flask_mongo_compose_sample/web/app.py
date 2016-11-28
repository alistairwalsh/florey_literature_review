from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo


app = Flask(__name__)


mongo = PyMongo(app)

@app.route('/info')
def info():
	username = "Alistair"
	user = mongo.db.users.find_one_or_404({'_id': username})
	return user

@app.route('/javascript')
def javascript():
    return render_template('javascript_tutorial.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def signin():
	return render_template('showSignUp.html')

# @app.route('/add_article', methods=['POST'])
# def add_article():
#   article = mongo.db.articles
#   name = request.json['name']
#   author = request.json['author']
#   article_id = article.insert({'name': name, 'author': author})
#   new_article = article.find_one({'_id': author_id })
#   output = {'name' : new_article['name'], 'author' : new_article['author']}
#   return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
