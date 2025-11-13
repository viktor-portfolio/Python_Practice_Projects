from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5

class LoginForm(FlaskForm):
    user_email = EmailField(label='Email', validators=[DataRequired(),
                                                       Email("Invalid email address.")])
    user_password = PasswordField(label='Password', validators=[DataRequired(),
                                                                Length(min=8, message="Field must be at least 8 character long.")])
    user_submit = SubmitField('Login')

app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "hello-people-keep-it-a-secret"



@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.user_email.data == 'admin@email.com' and login_form.user_password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
