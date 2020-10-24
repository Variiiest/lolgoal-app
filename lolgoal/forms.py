from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateTimeField
from lolgoal.models import Project, Mentor, Student
class RegisterStudent(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')
    def validate_username(self, username):
        user = Student.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        Email = Student.query.filter_by(email=email.data).first()
        if Email:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginStudent(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SignUpMentor(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    confirm_policy= BooleanField('Confirm Policy', validators=[DataRequired()])

    submit = SubmitField('Sign Up')
    def validate_username(self, username):
        user = Mentor.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        Email = Mentor.query.filter_by(email=email.data).first()
        if Email:
            raise ValidationError('That email is taken. Please choose a different one.')

    
class LoginMentor(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SubmitProject(FlaskForm):
    name = StringField('Name of Project',
                           validators=[DataRequired(), Length(min=20, max=200)])
    topic = StringField('Catagory',
                        validators=[DataRequired(), Length(min=10, max= 200)])
    price= IntegerField('Price of project', validators=[DataRequired()])
    add_on= DateTimeField('When you have completed?')
    duration= IntegerField('Duration of project in days', validators=[DataRequired()])
    description= TextAreaField('Summary', validators=[DataRequired(), Length(min=20, max=3000)])
    submit = SubmitField('Create')

