# Flask API Template

This is a project template for an API build in Flask.

## Install

**Clone the Repository:**

```bash
git clone git@github.com:19TT94/flask-api-template.git
cd flask-api-template
```

**Database**
This template version requires a running PostgreSQL instance available.
To build and run a db instance use the following.

```zsh
docker run --name postgres-db -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
```

**Configure the .env**

```zsh
cp env_example .env
```

- Update the env file with credentials to your local Postgres Database.
- Add a "Super User", this user will be created by the seeder, so there is always existing user credentials.

If you are following the instructions from the parent repo, follow the steps below otherwise.

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

**Initialize the Databases**

The api is configured for a live and test db. Create a database using the `create-db` command with the `--test` flag for a test db.

Note: This command _WILL_ delete any existing data in the database and should only be ran once.

```zsh
docker exec -it flask-api-template flask create-db --test
```

**Migrations**

The api uses [Flask Migrate](https://flask-migrate.readthedocs.io/en/latest/) and [Alembic](https://alembic.sqlalchemy.org/en/latest/) to run migrations.

In order to run a migration run

```zsh
docker exec -it flask-api-template flask db upgrade
```

To create a new migration run

```zsh
docker exec -it flask-api-template flask db migrate -m "{message to describe migration}"
```

**Seeders**

In order to run the seeder use the `db-seed` commnad. If you add the `--dev` flag it will seed the database with test data.

```zsh
docker exec -it flask-api-template flask db-seed
```

Note: This command _WILL_ delete any existing data in the database and should only be ran once.

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
