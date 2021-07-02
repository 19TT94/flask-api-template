# Flask API Template

This is a project template for an API build in Flask.

## Install

**Clone the Repository:**

```bash
git clone git@github.com:19TT94/flask-api-template.git
cd flask-api-template
```

**Configure the .env**

```zsh
cp env_example .env
```

## Run with Docker

```zsh
docker build -t {image_name} -f {docker_file} .
docker run -it --rm -v ${PWD}:/flask-api-template -p 5000:5000 {image_name}
```

At this point the API should be running.

## Commands

The available api commands can be found by running

```zsh
docker exec -it flask-api-template flask --help
```

**Generate Key**

The project requires an api key to specified in the `.env`. This can be generated using the command

```zsh
docker exec -it flask-api-template flask generate_key
```

Copy the key from the console and add it to your `.env`'s `SECRET_KEY`

## Testing

There are commands available via Flask for testing and test coverage.

To run the tests

```zsh
# all tests
docker exec -it flask-api-template flask test
# specific
docker exec -it flask-api-template flask test api/tests/{test_file_name}
# coverage
docker exec -it flask-api-template flask cov
```

## Run the API as a "Detached Service"

If you prefer to run the application without docker remove the Dockerfiles and follow the commands below.

**Create a virtualenv and activate it:**

```zsh
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
pip install -e .
cp env_example .env
# configure settings in newly created env file
```

## Run

`flask run`

## Test

`pytest`

**Run with coverage report:**

```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```
