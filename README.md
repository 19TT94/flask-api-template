# Hero Builder API - Flask API

This project was bootstrapped with Flask. It makes use of [FlaskRESTful](https://flask-restful.readthedocs.io/en/latest/quickstart.html) serves as the backend for the Hero Builder product. Hero Builder is, generally speaking, a form builder and scheduling app for managing Water/Wastewater Treatment Facilities.

# Development

This project relies on the [Hero Builder Client](https://github.com/Hero-Services/hero-builder-client) user facing code in the browser. In order to run the full environment please follow the steps to set up the api as well. You can run each service separatly or use the docker-compose file found the [Hero BUilder](https://github.com/Hero-Services/hero-builder) parent repo.

## Install

**Clone the Repository:**

```bash
git clone git@github.com:Hero-Services/hero-builder-api.git
cd flask-api-template
```

**Configure the .env**

```bash
cp env_example .env
```

- Update the env file with credentials to your local Postgres Database.
- Add a "Super User", this user will be created by the seeder, so there is always existing user credentials.

If you are following the instructions from the parent repo, follow the steps below otherwise.

## Run with Docker

```bash
docker build -t hero-builder-api
docker run -it --rm -v ${PWD}:/hero-builder-api -p 5000:5000 hero-builder-api
```

At this point the API should be running.

## Commands

The available api commands can be found by running

```bash
docker exec -it hero-builder-api flask --help
```

**Generate Key**

The project requires an api key to specified in the `.env`. This can be generated using the command

```bash
docker exec -it hero-builder-api flask generate_key
```

Copy the key from the console and add it to your `.env`'s `SECRET_KEY`

**Initialize the Databases**

The api is configured for a live and test db. Create a database using the `create-db` command with the `--test` flag for a test db.

Note: This command _WILL_ delete any existing data in the database and should only be ran once.

```bash
docker exec -it hero-builder-api flask create-db --test
```

**Migrations**

The api uses [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) and [Alembic](https://alembic.sqlalchemy.org/en/latest/) to run migrations.

In order to run a migration run

```bash
docker exec -it hero-builder-api flask db upgrade
```

To create a new migration run

```bash
docker exec -it hero-builder-api flask db migrate -m "{message to describe migration}"
```

**Seeders**

In order to run the seeder use the `db-seed` commnad. If you add the `--dev` flag it will seed the database with test data.

```bash
docker exec -it hero-builder-api flask db-seed
```

Note: This command _WILL_ delete any existing data in the database and should only be ran once.

**Create your super user**
Run the following command to create your user:

```bash
docker exec -it hero-builder-api flask create-user --super
```

## Testing

There are commands available via Flask for testing and test coverage.

To run the tests

```bash
# all tests
docker exec -it hero-builder-api flask test
# specific
docker exec -it hero-builder-api flask test api/tests/{test_file_name}
# coverage
docker exec -it hero-builder-api flask cov
```

## Run the API as a "Detached Service"

**Create a virtualenv and activate it:**

```bash
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
