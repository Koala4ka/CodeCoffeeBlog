from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from models import User


class LoginForm(FlaskForm):
    username = StringField('Юзернейм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти (в IT)')
    error = ''  # todo: fix; i'm not sure what's the proper way to pass error like incorrect password hence doing it like so for now


class SignupForm(FlaskForm):
    username = StringField('Юзернейм', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Пароль ещё раз', validators=[DataRequired()])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Этот юзернейм уже занят :(')
