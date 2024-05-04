from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, NumberRange, Email, Optional
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    """Register Form"""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(min=1, max=20)],
                             )

    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=55)],
                             )
    
    email = StringField('Email', validators=[InputRequired(), Length(max=50)],
                        )

    first_name = StringField('First Name', validators=[InputRequired(), Length(max=20)],
                             )

    last_name = StringField('Last Name', validators=[InputRequired(), Length(max=20)],
                             )
    
class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField('Username', validators=[InputRequired()])

    password = PasswordField('Password', validators=[InputRequired()])

class DeleteForm(FlaskForm):
    """Delete Account Confirmation Form"""

class FeedbackForm(FlaskForm):
    """Form to give feedback"""

    title = StringField(
        "Title",
        validators=[InputRequired(), Length(max=100)],
    )
    content = StringField(
        "Content",
        validators=[InputRequired()],
    )

