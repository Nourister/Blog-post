from website import app, db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'a9d108e0e581ba50aa01bf74aa60c9ac'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_site.db'
db = SQLAlchemy(app)


# Import models
from website.models import Post, User

# Cretae database tables if do not exit
with app.app_context():
    db.create_all()

# Import routes
from website import routes