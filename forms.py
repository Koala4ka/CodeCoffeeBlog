from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from models import User

def dataRequired():
    return DataRequired(message='Это поле не должно быть пустым')

class LoginForm(FlaskForm):
    username = StringField('Юзернейм', validators=[dataRequired()])
    password = PasswordField('Пароль', validators=[dataRequired()])
    submit = SubmitField('Войти (в IT)')


class SignupForm(FlaskForm):
    username = StringField('Юзернейм', validators=[dataRequired()])
    password = PasswordField('Пароль', validators=[dataRequired()])
    password2 = PasswordField('Пароль ещё раз', validators=[dataRequired(), EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Регистрация')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Этот юзернейм уже занят :(')
