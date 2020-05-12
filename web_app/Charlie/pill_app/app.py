from flask import Flask, render_template, redirect, url_for, send_file, render_template_string, request
from datetime import datetime, timedelta
from flask_mail import Message
from flask_mail import Mail
import webbrowser
import CompiledCode as cc
import time
import csv
import numpy as np

app = Flask(__name__)
mail = Mail(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


# Set up title, headers, etc for home page
def template(title = "pill web app", text = "Home Page"):
    now = datetime.now()
    timeString = now.strftime("%-I:%M %p")
    day = now.strftime("%A")
    dateString = now.strftime("%B %-d, %Y")
    templateData = {
        'title' : title,
        'time' : timeString,
        'day' : day,
        'text' : text,
        'date' : dateString
        }
    return templateData

def verification(title):
    now = datetime.now()
    timeString = now.strftime("%-I:%M %p")
    day = now.strftime("%A")
    dateString = now.strftime("%B %-d, %Y")
    
    tomorrow = datetime.now() + timedelta(days = 1)
    tomorrow = tomorrow.strftime("%B %-d, %Y")
    scheduled_time = str("9:00 am")
    
    templateData = {
        'title' : title,
        'time' : timeString,
        'day' : day,
        'date' : dateString,
        'next_day' : tomorrow,
        'schd_t' : scheduled_time
        }
    return templateData
# Set home page
@app.route("/")
def home():
    templateData = template()
    return render_template('HomePage.html',**templateData)

@app.route("/takeMeds")
def runDispenser():
    return render_template('loading_page.html')

@app.route("/results")
def results():
    templateData = verification("Verification")
    return render_template('results.html', **templateData)

@app.route("/contact")
def contact():
    templateData = template()
    return render_template('contact.html', **templateData)

@app.route("/lit_photo")
def light_photo():
    path = 'lit_photo.jpg'
    return send_file(path)

#Steve's processing pages
@app.route("/processing")
def processing_home():
    templateData = template()
    return render_template('pillprocessing.html', **templateData)

@app.route("/homebutton")
def home_back():
    templateData = template()
    return render_template('pillprocessing.html', **templateData)

@app.route("/handle_data", methods=['POST'])
def handle_data():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    print(name)
    print(email)
    print(message)
    #msg = Message(message, sender=(name, email),recipients=["charliefisher11@icloud.com"])
    #mail.send(msg)
    return render_template('sent_email.html')

def list_csv():
    output = []
    with open('medication_list.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            output.append(row)
        return output


    
@app.route("/list")
def list():
    templateData = template("Prescription List")
    output = list_csv()
    return render_template('medication_list.html', output = output, **templateData)

@app.route("/addmeds")
def addmeds():
    templateData = template("Add Medication")
    output = list_csv()
    return render_template('add_meds.html', output=output, **templateData)

@app.route("/addnewmeds", methods = ['POST'])
def newMeds():
    meds = request.form['meds']
    dose = str(request.form['dose'])
    dose_units = request.form['dose units']
    dose = dose + dose_units
    freq = request.form['freq'] +'\n'
    new_meds = [meds, dose, freq]
    output = list_csv()
    duplicate = False 
    for row in output:
        if (np.array_equal(row, new_meds)):
            duplicate = True
            # user typed in same meds return an error
    if not duplicate:
        with open('medication_list.csv','a', newline = '') as f:
            writer=csv.writer(f)
            writer.writerow(new_meds)
    templateData = template("Add Medication")
    new_output = list_csv()
    return render_template('add_meds.html', output=new_output, **templateData)

"""
@app.route("/scanpill")
def scan():
    num_pills = cc.scan_pill()
    message = "Found " + str(num_pills) + " pill(s)"
    templateData = template(text = message)
    return render_template('main.html', **templateData)
    
@app.route("/picsonly")
def pics():
    num_pills = cc.pics_only()
    message = "Found " + str(num_pills) + " pill(s)"
    templateData = template(text = message)
    return render_template('main.html', **templateData)
    
@app.route("/analyze")
def run_analysis():
    a, pill_index = cc.analysis(True)
    message = "Analyzed pill #" + str(pill_index-1)
    templateData = template(text = message)
    return render_template('main.html', **templateData)
    
@app.route("/databasematch")
def find_match():
   
    cc.finalize_database()
    
    message, pi = cc.analysis(False)
    templateData = template(text = "This is pill #" + str(message))
    return render_template('main.html', **templateData)

@app.route("/finalpill")
def show_pill():
    path = cc.get_path()
    return send_file(path)
    
@app.route("/qrimage")
def show_qr():
    path = 'images/qr_code.jpg'
    return send_file(path)



"""

if __name__ == '__main__':
    webbrowser.open_new("http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0')



 
