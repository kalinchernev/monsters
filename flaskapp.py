from flask import Flask, request, session, flash, url_for, redirect, \
     render_template, abort, send_from_directory, json

from flask_oauth import OAuth


app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')


# Taking configs from client_secrets.json
CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']

CLIENT_SECRET = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_secret']

REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console

oauth = OAuth()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=CLIENT_ID,
                          consumer_secret=CLIENT_SECRET)


@google.tokengetter
def get_access_token():
    return session.get('access_token')


@app.route('/')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    return res.read()
    # return render_template('index.html')


@app.route('/login')
def login():
    callback = url_for('authorized', _external=True)
    return google.authorize(callback=callback)


@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))


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
    if username == 'tomi':
        return render_template('people/profile-tomi.html')
    elif username == 'alex':
        return render_template('people/profile-alex.html')
    else:
        return redirect(url_for('people'))


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
