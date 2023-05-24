from werkzeug.security import generate_password_hash
from faker import Faker
from .models import Client, City, User
from app import db

def seed_data():
    fake = Faker()

    # Agregar algunas ciudades
    city1 = City(cod=1, name='New York')
    city2 = City(cod=2, name='Los Angeles')
    city3 = City(cod=3, name='Chicago')

    db.session.add(city1)
    db.session.add(city2)
    db.session.add(city3)

    # Agregar algunos clientes
    for i in range(4, 104):  # Creará 100 clientes
        client = Client(cod=i, name=fake.name(), city_cod=fake.random_int(min=1, max=3))
        db.session.add(client)

    # Agregar algunos usuarios
    password_hash = generate_password_hash('admin')
    user1 = User(name='admin', password=password_hash, email='admin@example.com', photo=None)

    db.session.add(user1)

    db.session.commit()

# Ejecutar la función de sembrado
if __name__ == "__main__":
    seed_data()
