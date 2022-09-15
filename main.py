from flask import Flask, render_template, request, redirect, url_for
from wtforms import StringField, validators, SubmitField
from flask_wtf import Form

app = Flask(__name__)


class GreetForm(Form):
    name = StringField('Username', validators=[validators.data_required()])
    submit = SubmitField('Submit')

class Morse(Form):
    text = StringField("What to translate?", validators=[validators.data_required()])
    submit = SubmitField('Submit')


@app.route('/', methods=["GET", "POST"])
def index():
    name = None
    form = GreetForm(request.form)
    if form.validate:
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/morse', methods=["GET", "POST"])
def morse():
    form = Morse()
    translation = None
    if form.validate():
        print(form.text.data)
        translation = form.text.data
        translation = ''
        print(translation)
    return render_template('morse.html', form=form, translation=translation)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == ("__main__"):
    app.run(debug=True)