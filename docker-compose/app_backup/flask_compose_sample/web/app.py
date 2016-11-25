from flask import Flask, render_template
import sys
import optparse
import time

app = Flask(__name__)

start = int(round(time.time()))

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

