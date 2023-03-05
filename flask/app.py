from flask import Flask, url_for, render_template
from influx_db import DbCon

app = Flask(__name__)
css = None

chef = DbCon()

@app.route('/')
def index():
    return render_template('index.html', objects=chef.get_topics())