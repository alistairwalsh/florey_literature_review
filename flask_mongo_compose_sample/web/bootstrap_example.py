from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template("boot_index.html")

@app.route('/javascript')
def javascript():
    return render_template('javascript_tutorial.html')

@app.route('/showSignUp')
def signin():
	return render_template('showSignUp.html')    

if __name__ == "__main__":
	app.run()