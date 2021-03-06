from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, IntegerField, FloatField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms_components import DateRange
from datetime import date
from flasktrainingcalendar.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
    
class LoginForm(FlaskForm):
    username_or_email = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
    
class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')
            
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
                
class NewWorkoutForm(FlaskForm):
    workout_type=SelectField('Workout Type', choices=[('run', 'run'), ('slow run', 'slow run'), ('tempo run', 'tempo run'), ('interval workout', 'interval workout'), ('fartlek', 'fartlek')],validators=[DataRequired()])
    workout_distance=FloatField('Workout Distance', validators=[DataRequired()])
    distance_unit=SelectField('Unit Of Measurement', choices=[('K', 'kilometres'), (' mile', 'miles'), (' metre', 'metres')],validators=[DataRequired()])
    target_date=DateField('Target Date', format='%Y-%m-%d', validators=[DataRequired()])
    description=TextAreaField('Description')
    submit=SubmitField('Add Workout')
    
class CompletedWorkoutForm(FlaskForm):
    submit=SubmitField('Completed')
    
class WorkoutPhotoForm(FlaskForm):
    picture = FileField('Upload A Workout Photo', validators=[DataRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    upload = SubmitField('Upload')
    
class RequestResetForm(FlaskForm):
    username_or_email = StringField('Username or Email', validators=[DataRequired()])
    submit=SubmitField('Request Password Reset')
    
    def validate_user(self, email):
        user = User.query.filter_by(email=username_or_email.data).first()
        if user is None:
            user = User.query.filter_by(username=username_or_email.data).first()
            if user is None:
                raise ValidationError('That account does not exist. You must register first.')
            
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField('Reset Password')
    
class UserSearchForm(FlaskForm):
    search = StringField('Search for a user', validators=[DataRequired()])
    submit=SubmitField('Search')
    
class CommentForm(FlaskForm):
    comment = StringField('Enter a comment', validators=[DataRequired(), Length(max=300)])
    submit_comment = SubmitField('Post Comment')
    
class EditCommentForm(FlaskForm):
    comment = StringField('Edit your comment', validators=[DataRequired(), Length(max=300)])
    submit_update = SubmitField('Update Comment')