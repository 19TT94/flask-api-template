import os, click, uuid
from werkzeug.security import generate_password_hash
from faker import Faker

from api import db, create_app
from api.database.models.user import User
from api.database.models.department import Department
from api.database.models.user_role import UserRole
from api.database.models.facility import Facility
from api.database.models.facility_user import FacilityUser

fake = Faker()

# Config Variables
db_user =  os.environ.get("POSTGRES_USER")
db_password = os.environ.get("POSTGRES_PASSWORD")
db_host = os.environ.get("POSTGRES_HOST")
db_port = os.environ.get("POSTGRES_PORT")
db_name = os.environ.get("POSTGRES_DB")

@click.command()
@click.option(
    "--super",
    "-s",
    "super_",
    is_flag=True,
    default=False,
    help="Create a Super User."
)
@click.option(
    "--test",
    "-t",
    is_flag=True,
    default=False,
    help="Create a test user. All details other than password will be automatically generated"
)
def create_user(super_: bool=False, test: bool=False) -> None:
    """
    Add a user to the database

    :param super: Create a super user.
    :param test: Short cut for creating test users.
    :return: None
    """

    db_uri = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        db=db_name
    )

    params = {}
    params["SQLALCHEMY_DATABASE_URI"] = db_uri

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    departments = [department.id for department in Department.get_all()]
    roles = [role.id for role in UserRole.get_all()]

    password = click.prompt('Please enter a password', type=str, hide_input=True, confirmation_prompt=True)
    hashed = generate_password_hash(password, method="sha256") 

    user_type = 1
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    department = fake.random_element(elements=departments)
    role = fake.random_element(elements=roles)

    if not test:
        email = click.prompt('Please enter a valid email', type=str)
        first_name = click.prompt('Please enter your first name', type=str)
        last_name = click.prompt('Please enter your last name', type=str)

    if super_:
        user_type = 4
        department = 1
        role = 1

    user_params = {
        "public_id": str(uuid.uuid4()),
        "user_type_id": user_type,
        "email": email,
        "password": hashed,
        "first_name": first_name,
        "last_name": last_name,
        "user_department_id": department,
        "user_role_id": role,
        "is_invited": False,
        "is_active": 1
    }

    try:
        new_user = User(**user_params)
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        raise e

    if super_:
        facilities = Facility.get_all()
        for facility in facilities:
            facility_user_params = {
                "facility_id": facility.id,
                "user_id": new_user.id
            }
            facilityUser = FacilityUser(**facility_user_params)
            db.session.add(facilityUser)
            db.session.commit()

    click.echo("User {0} {1} created.".format(first_name, last_name))

    ctx.pop()
