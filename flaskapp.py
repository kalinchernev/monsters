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


@app.route("/people")
def people():
    return render_template('people/people.html')


@app.route("/people/<username>")
def profile(username):
    if username == 'tomi':
        return render_template('people/profile-tomi.html')
    elif username == 'alex':
        return render_template('people/profile-alex.html')
    else:
        return redirect(url_for('people'))


@app.route("/about")
def about():
    return render_template('pages/about.html')


@app.route("/contacts")
def contacts():
    return render_template('pages/contacts.html')


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('templates/pages/404.html'), 404

if __name__ == '__main__':
    app.run()
