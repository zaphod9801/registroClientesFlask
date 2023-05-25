from app import db


class Client(db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city_cod = db.Column(db.Integer, db.ForeignKey('city.cod'), nullable=False)

    def to_dict(self):
        data = {
            'cod': self.cod,
            'name': self.name,
            'city_cod': self.city_cod
        }
        return data


class User(db.Model):
    name = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    photo = db.Column(db.String(50), nullable=True)

    def to_dict(self):
        data = {
            'name': self.name,
            'email': self.email
        }
        return data


class City(db.Model):
    cod = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    clients = db.relationship('Client', backref='city', lazy=True)

    def to_dict(self):
        data = {
            'cod': self.cod,
            'name': self.name,
            'clients': list(map(lambda a: a.to_dict(), self.clients))
        }
        return data
