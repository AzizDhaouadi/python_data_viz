# Importing Required Modules for the App
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
from dash.dependencies import Input, Output

import flask
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email
import email_validator

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

class contactForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)], name='Inputemail')
    message= TextAreaField(label='Your Message')
    submit = SubmitField(label="Send Message")

server = flask.Flask(__name__)
server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///requests.db'

#Initialize the database
db = SQLAlchemy(server)

#Create db model
class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_received = db.Column(db.DateTime, default=datetime.utcnow)

    #Create function to return messages when values are added
    def __repr__(self):
        return '<Name %r' % self.id


server.secret_key = "g?@jY6@yN9GXxBGcJ45BfmbDrfX5Fk&didn#MbD8"



@server.route('/', methods=["GET", "POST"])
def home():
    form = contactForm()
    if form.validate_on_submit():
        print(f"E-mail:{form.email.data}, message:{form.message.data}")
        request = Requests(email=form.email.data, message=form.message.data)
        try:
            db.session.add(request)
            db.session.commit()
            form.email.data = ''
            form.message.data = ''
            return redirect(url_for('home'))
        except:
            for error in form.errors.itervalues():
                flash(error[0])
            return "There was an error. Please try again later."

    return render_template('home.html',form=form)

@server.route('/docs')
def docs():
    return render_template('docs.html')


external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=Tangerine&display=swap',
    {
        'href': 'https://fonts.googleapis.com/css2?family=Tangerine&display=swap',
        'rel': 'stylesheet',
        'crossorigin': 'anonymous'
    },

    'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Mono:ital,wght@1,100&display=swap',

    {
        'href': 'https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto+Mono:ital,wght@1,100&display=swap',
        'rel': 'stylesheet',
        'crossoriging': 'anonymous'
    },

    'static/bootstrap.min.css',
    {
        'href': 'static/bootstrap.min.css',
        'rel': 'stylesheet',
        'crossorigin': 'anonymous'
    },

]



# Initializing the App
app = dash.Dash(__name__,  external_stylesheets=external_stylesheets, title='Python Data Visualization - Plotly & Dash Dashboard', suppress_callback_exceptions=True,server=server)

server = app.server


