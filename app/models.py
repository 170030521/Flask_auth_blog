from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Blog(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    title=db.Column(db.String(80),nullable=False)
    content=db.Column(db.Text,unique=True,nullable=False)
    # age=db.Column(db.Integer,nullable=False)
    # password=db.model(db.String(120),nullable=False)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(80),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    # password=db.model(db.String(120),nullable=False)


