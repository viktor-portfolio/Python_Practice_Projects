from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps(URL)', validators=[DataRequired()])
    opening = TimeField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing = TimeField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    rating = SelectField('Coffee Rating', choices=[('☕','1'), ('☕☕','2'), ('☕☕☕','3'), ('☕☕☕☕', '4'), ('☕☕☕☕☕', '5')])
    wifi = SelectField('Wifi Strength Rating', choices=[('✘','✘'),('💪','1'), ('💪💪','2'), ('💪💪💪','3'), ('💪💪💪💪', '4'), ('💪💪💪💪💪', '5')])
    power = SelectField('Power Socket Availability', choices=[('✘', '✘'),('🔌','1'), ('🔌🔌','2'), ('🔌🔌🔌','3'), ('🔌🔌🔌🔌', '4'), ('🔌🔌🔌🔌🔌', '5')])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.opening.data,
                form.closing.data,
                form.rating.data,
                form.wifi.data,
                form.power.data
            ])
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form)


@app.route('/cafes', methods=['GET', 'POST'])
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
