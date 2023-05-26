from app import db, app
from Backend.models import models
from Backend.models import seeder

with app.app_context():
    db.create_all()
    seeder.seed_data()
