from flask import Flask, render_template, request, redirect, url_for, flash
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
    
@app.route('/add_author', methods=['GET', 'POST'])
def add_author():
    if request.method == 'POST':
        name = request.form['name']
        new_author = Author(name=name)
        db.session.add(new_author)
        db.session.commit()
        flash('Author added successfully!')
        return redirect(url_for('add_author'))
    return render_template('add_author.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    authors = Author.query.all()
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        new_book = Book(title=title, author_id=author_id)
        db.session.add(new_book)
        db.session.commit()
        flash('Book added successfully!')
        return redirect(url_for('add_book'))
    return render_template('add_book.html', authors=authors)

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('home.html', books=books)