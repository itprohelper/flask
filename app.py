# Flask app for catalog items

from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
# from sqlalchemy import create_engine, asc
# from sqlalchemy.orm import sessionmaker
# from database_setup import Base, Category, Item, User

app = Flask(__name__)

@app.route('/')
@app.route('/category/')
def showCategories():
    return 'Hola home and category'

@app.route('/test')
def showTest():
    return 'This is a test'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
