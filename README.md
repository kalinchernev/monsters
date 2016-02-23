# Flask-based prototype

[![Join the chat at https://gitter.im/kalinchernev/monsters](https://badges.gitter.im/kalinchernev/monsters.svg)](https://gitter.im/kalinchernev/monsters?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Requirements
- [python](https://www.python.org/downloads/)

Recommended
- [virtualenv](http://virtualenv.readthedocs.org/en/latest/installation.html)

## Documentation
- [Flask](http://flask.pocoo.org/docs/0.10/)
- [Creating a new URL serving a template](http://flask.pocoo.org/docs/0.10/quickstart/#rendering-templates)

## Local dev environment
In the command line:

- `git clone git@github.com:kalinchernev/monsters.git`
- `cd monsters`
- `virtualenv env` creates compartmentized local dev environment
- `source env/bin/activate` where the env is the local dev environment

The cli should give a hint for successful activation

```bash
(env) kalin@pc-name:~/projects/monsters$
```
Now packages and dependencies will stay in this isolated dev environment.

## Installing a package

```bash
(env) kalin@pc-name:~/projects/monsters$ pip install flask-script
```
Where flask-script is an example package.

## Installing dependencies

```bash
(env) kalin@pc-name:~/projects/monsters$ pip install -r requirements.txt
```

## Local server
Start a local webserver by running:

```bash
python app.py
```

## License
This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to CC0 (http://creativecommons.org/publicdomain/zero/1.0/)

## Credits
[Openshift love for Flask](https://developers.openshift.com/en/python-flask.html)
