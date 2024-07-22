from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a9d108e0e581ba50aa01bf74aa60c9ac'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_site.db'

    db.init_app(app)

    with app.app_context():
        from app import routes
        from app.models import Post, User
        db.create_all()

    return app