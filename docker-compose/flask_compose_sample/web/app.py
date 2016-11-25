from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/javascript')
def javascript():
    return render_template('javascript_tutorial.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showSignUp')
def signin():
	return render_template('showSignUp.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
