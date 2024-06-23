#SDEV220_10P_M04_CaseStudy
#Tracie Lindquist
#Create an API in Python for books
#API should contain book id, book name, book author, book publisher

import requests
import json

# create our own API
from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy



#define the database engine
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

#create the class for the database and define the attributes, and constraints
class Book(db.Model): 
    """A class that creates the book database, defines attributes and constraints"""
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(120), nullable = False)
    publisher = db.Column(db.String(150), nullable = False)
    
    def __repr__(self):
        return f'{self.book_name} - {self.author}'
    
#test    


@app.route('/')
def index():
    return "Hello"

#query the book database to return a list of all books 
@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)
    return {'books' : output}

#search for a book by book idt
@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}

#create a new entry in the book database
@app.route('/books', methods = ['POST'])
def add_books(): 
    book = Book(book_name = request.json['name'], author =  request.json['author'], publisher = request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

with app.app_context():
    db.create_all()