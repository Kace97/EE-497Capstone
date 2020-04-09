from flask import Flask, render_template, redirect, url_for, send_file
import datetime

app = Flask(__name__,template_folder='Templates/')

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

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')

# Set home page
@app.route("/")
def hello():
    templateData = template()
    return render_template('main.html', **templateData)

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

if __name__ == "__main__":        
    app.run() 





