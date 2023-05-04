from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here
scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
scheduler.start()
def work_time():
    print("Hello")
scheduler.add_job(work_time, trigger='cron', hour=14, minute=5)
 
@app.route('/')
def welcome():
    return render_template('home.html')
  
if __name__=="__main__":
    app.run(debug=False)
