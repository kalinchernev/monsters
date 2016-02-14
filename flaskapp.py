import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/leaders")
def leaders():
    return render_template('leaders.html')


@app.route("/teams/<team_name>")
def teams(team_name):
    return render_template('team.html', team_name=team_name)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contacts")
def contacts():
    return render_template('contacts.html')


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()
