
#import RPI.GPIO as GPIO
from flask import Flask, session, abort, render_template, redirect, url_for, send_file, flash, request, \
    send_from_directory
import datetime
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# #define actuators GPIOs
# motorOne = 13
# motorTwo = 19
#
# #initialize GPIO status variables
# motorOneSts = 0
# motorTwoSts = 0
#
# # Define motor pins as output
# GPIO.setup(motorOne, GPIO.OUT)
# p = GPIO.PWM(motorOne, 50)
# GPIO.setup(motorTwo, GPIO.OUT)
# p = GPIO.PWM(motorTwo, 50)
#
# # turn motors OFF
# GPIO.output(motorOne, GPIO.LOW)
# GPIO.output(motorTwo, GPIO.LOW)


# Set up title, headers, etc for home page
def template(title = "PILL WEB APP"):
    now = datetime.datetime.now()
    timeString = now
    templateData = {
        'title' : title,
        'time' : timeString
        }
    return templateData


@app.route('/')
def home():
    templateData = template()

    return render_template('index.html', **templateData)


@app.route("/reminder")
def reminder():

    templateData = template(title='Reminder')
    return render_template('reminder.html', **templateData)

@app.route("/notify")
def notify():
    # message = "Time to Take Pills!"
    #
    # templateData = template(title='Notification', text = message)
    return render_template('notification.html')

@app.route("/control")
def control():
    message = "Click to Deliver Pills!"

    # if action == "on":
    #     GPIO.output(motorOne, GPIO.HIGH)
    # if action == "off":
    #     GPIO.output(motorTwo, GPIO.LOW)
    #
    # motorOneSts = GPIO.input(ledRed)
    # motorTwoSts = GPIO.input(ledYlw)
    #
    # templateData = {
    #     'ledRed': ledRedSts,
    #     'ledYlw': ledYlwSts,
    # }
    templateData = template()
    return render_template('control.html', **templateData)


if __name__ == "__main__":
    app.run() 

