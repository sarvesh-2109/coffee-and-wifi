from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL(require_tld=True)])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',
                                choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),
                                         ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')])

    wifi_strength = SelectField('WiFi Strength Rating',
                                choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'),
                                         ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪')])

    power_socket = SelectField('Power Socket Rating',
                               choices=[('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                        ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            csv_writer.writerow([form.cafe_name.data, form.cafe_location.data,
                                 form.opening_time.data, form.closing_time.data,
                                 form.coffee_rating.data, form.wifi_strength.data,
                                 form.power_socket.data])
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
