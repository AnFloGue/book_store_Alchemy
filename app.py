from flask import Flask
from data_models import db, Author, Book
import os

database_dir = os.path.join(os.getcwd(), 'data')
if not os.path.exists(database_dir):
    os.makedirs(database_dir)
    print(f"Created directory: {database_dir}")

database_file = f"sqlite:///{os.path.join(database_dir, 'library.sqlite')}"
print(f"Database file path: {database_file}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Configured SQLALCHEMY_DATABASE_URI")

with app.app_context():
    db.init_app(app)
    db.create_all()  