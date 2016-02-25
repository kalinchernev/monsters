from flask import Flask, request, session, flash, url_for, redirect, \
     render_template, abort, send_from_directory

import random, string

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(32))
    session['state'] = state
    return state


@app.route("/classes")
def classes_overview():
    return render_template('classes/classes_overview.html')


@app.route("/classes/<class_name>")
def teams(class_name):
    return render_template('classes/class.html', class_name=class_name)


@app.route("/lessons")
def lessons_overview():
    return render_template('lessons/lessons_overview.html')


@app.route("/lessons/<lesson_name>")
def lesson_page(lesson_name):
    return render_template('lessons/lesson.html', lesson_name=lesson_name)


@app.route("/people")
def people():
    return render_template('people/people.html')


@app.route("/people/<username>")
def profile(username):
    return render_template('people/profile.html', username=username)


@app.route("/leaders")
def leaders():
    return render_template('pages/leaders.html')


@app.route("/monster")
def monster():
    return render_template('pages/monster.html')


@app.route("/about")
def about():
    return render_template('pages/about.html')


@app.route("/contacts")
def contacts():
    return render_template('pages/contacts.html')


@app.route("/roadmap")
def roadmap():
    return render_template('pages/roadmap.html')


@app.route('/<path:resource>')
def serveStaticResource(resource):
    return send_from_directory('static/', resource)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


if __name__ == '__main__':
    app.run()
