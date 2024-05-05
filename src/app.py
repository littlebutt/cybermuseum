from flask import Flask, render_template


app = Flask(__name__)


@app.route('/unix-v1')
def unix_v1():
    return render_template('unix-v1.html')


@app.route('/python-091')
def python_0_9_1():
    return render_template('python-091.html')
