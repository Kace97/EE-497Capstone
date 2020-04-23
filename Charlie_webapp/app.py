from flask import Flask, render_template, redirect, url_for, send_file, render_template_string
import datetime
import requests
import remi.gui as gui
from remi import start, App
import webbrowser
"""
class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=120, height=100)
        self.lbl = gui.Label('Hello world!')
        self.bt = gui.Button('Press me!')

        # setting the listener for the onclick event of the button
        self.bt.onclick.do(self.on_button_pressed)

        # appending a widget to another, the first argument is a string key
        container.append(self.lbl)
        container.append(self.bt)

        # returning the root widget
        return container

    # listener function
    def on_button_pressed(self, widget):
        self.lbl.set_text('Button pressed!')
        self.bt.set_text('Hi!')

    

# starts the web server
start(MyApp)

"""

app = Flask(__name__)

# Set up title, headers, etc for home page
def template(title = "PILL WEB APP", text = "Home Page"):
    now = datetime.datetime.now()
    timeString = now
    templateData = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateData

# Set home page
@app.route("/")
def home():
    templateData = template()
    return render_template('index.html', **templateData)

@app.route("/button2")
def button2():
    message = "You went to page two"

    templateData = template(title='Sign up', text = message)
    return render_template('signup.html', **templateData)

if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0')

"""
# Set up title, headers, etc for home page
def template(title = "PILL WEB APP", text = "Home Page"):
    now = datetime.datetime.now()
    timeString = now
    templateData = {
        'title' : title,
        'time' : timeString,
        'text' : text
        }
    return templateData
@app.route("/data")
def index():
	# Read Sensors Status
	buttonSts = GPIO.input(button)
	senPIRSts = GPIO.input(senPIR)
	templateData = {
      'title' : 'GPIO input Status!',
      'button'  : buttonSts,
      'senPIR'  : senPIRSts
      }
	return render_template('index.html', **templateData)
@app.route("/button1")
def button1():
    message = "You went to page one"

    templateData = template(title='PAGE 1', text = message)
    return render_template('pageone.html', **templateData)

@app.route("/button2")
def button2():
    message = "You went to page two"

    templateData = template(title='PAGE 2', text = message)
    return render_template('pagetwo.html', **templateData)

@app.route("/homebutton")
def home():
    templateData = template()
    return render_template('main.html', **templateData)
"""
