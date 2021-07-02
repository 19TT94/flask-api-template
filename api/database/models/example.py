# No database by Default this an example Database Model that will not work
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Example(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    text  = db.Column(db.String)

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text
        }

    @classmethod
    def get_id(cls, _id: str) -> dict:
        return Example.query.filter_by(id=str(_id)).first()

    @classmethod
    def get_all(cls) -> dict:
        return Example.query.all()
