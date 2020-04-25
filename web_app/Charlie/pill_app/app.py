from flask import Flask, render_template, redirect, url_for, send_file, render_template_string
import datetime
import webbrowser
#import CompiledCode as cc
import os
import time

STATIC_DIR = os.path.abspath('/templates')
app = Flask(__name__, static_folder=STATIC_DIR)

# Set up title, headers, etc for home page
def template(title = "PILL WEB APP", text = "Home Page"):
    now = datetime.datetime.now()
    timeString = now.strftime("%I:%M:%S %p")
    dateString = now.strftime("%A, %B %-d, %Y")
    templateData = {
        'title' : title,
        'time' : timeString,
        'text' : text,
        'date' : dateString
        }
    return templateData

# Set home page
@app.route("/")
def home():
    templateData = template()
    return render_template('HomePage.html',**templateData)

@app.route("/takeMeds")
def runDispenser():
    templateData = template(text = "results")
    return render_template('loading_page.html')

@app.route("/results")
def results():
    return render_template("main.html")
"""
@app.route("/scanpill")
def scan():
    render_template('loading_page.html')
    num_pills = cc.scan_pill()
    message = "Found " + str(num_pills) + " pill(s)"
    templateData = template(text = message)
    return render_template('loading_page.html', **templateData)
"""
if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0')

 
