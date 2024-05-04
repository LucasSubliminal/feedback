from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect database to app file"""
    db.app = app
    db.init_app(app)

class User(db.Model):
    """User model for storing user data in the database."""
    __tablename__ = 'users'

    username = db.Column(db.String(20), primary_key=True, unique=True)

    password = db.Column(db.Text, nullable=False) 

    email = db.Column(db.String(50), nullable=False, unique=True) 

    first_name = db.Column(db.String(30), nullable=False) 

    last_name = db.Column(db.String(30), nullable=False) 

    @classmethod
    def register(cls, username, pwd, first_name, last_name, email):
        """Register user with a hashed password and returns user"""

        hashed = bcrypt.generate_password_hash(pwd)

        hashed_utf8 = hashed.decode('utf8')

        user = cls(
            username=username,
            password=hashed_utf8,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        db.session.add(user)
        
        feedback = db.relationship("Feedback", backref="user", cascade="all,delete")

    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists and password is correct"""

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False
class Feedback(db.Model):
    """Table for feedback"""

    __tablename__ = 'feedback'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)

    title = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text, nullable=False)

    username = db.Column(db.String(20),
                         db.ForeignKey('users.username'),
                         nullable=False)