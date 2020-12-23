# Flask API Template

This is a project template for an API build in Flask. It makes use of [FlaskRESTful](https://flask-restful.readthedocs.io/en/latest/quickstart.html).

## Install

```
git clone git@github.com:19TT94/flask-api-template.git
cd flask-api-template
python -m venv venv
. venv/bin/activate
pip install -e .

```

Install
Be sure to use the same version of the code as the version of the docs you're reading. You probably want the latest tagged version, but the default Git version is the master branch.

**Clone the Repository:**
```
git clone git@github.com:19TT94/flask-api-template.git
cd flask-api-template
```

**Create a virtualenv and activate it:**
```
python3 -m venv venv
. venv/bin/activate
$ pip install -e .
```

## Run
```
export FLASK_APP=api
export FLASK_ENV=development
flask run
```

## Test
`pytest`

**Run with coverage report:**
```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```