from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class OrderForm(FlaskForm):
    # validators=[DataRequired() проверяет не пустой ли поле
    usernameOrder = StringField('Имя', validators=[DataRequired()])
    addressOrder = StringField('Адрес', validators=[DataRequired()])
    phoneOrder = StringField('телефон', validators=[DataRequired()])
