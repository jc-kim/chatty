from wtforms import Form, StringField, PasswordField, validators


class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=255), 
                                        validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4),
                                          validators.DataRequired()])
    nickname = StringField('Nickname', [validators.Length(min=4, max=255),
                                        validators.DataRequired()])


class LoginForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=255), 
                                        validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=4),
                                          validators.DataRequired()])