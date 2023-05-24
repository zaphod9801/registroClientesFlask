from app import db


class Client(db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city_cod = db.Column(db.Integer, db.ForeignKey('city.cod'), nullable=False)


class User(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    photo = db.Column(db.String(50), nullable=True)


class City(db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    clients = db.relationship('Client', backref='city', lazy=True)
