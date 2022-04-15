from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User


class LoginForm (FlaskForm):
    username = StringField('Username :', validators=[DataRequired()])
    password = PasswordField('Password :', validators=[DataRequired()])
    remember_me = BooleanField('Remember me :')
    submit = SubmitField('Sign-In')


class RegestriationForm(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password: ', validators=[
                              DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    # to check if there is any user with the same username

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This name is takken, use another name.')
    # to check if there is  any error with the same email

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'This email is takken before or wrong please try again.')


class EditProfileClass(FlaskForm):
    username = StringField('Username: ', validators=[DataRequired()])
    about_me = TextAreaField('About me:', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
#to prevent duplication on the username while change it 
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileClass, self).__init__(original_username, *args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')