from flask import Flask, render_template, request
from API import solar_api as solar , events_api as event_api

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("base.html")

@app.route("/gallery", methods=["GET","POST"])
def gallery():
    if request.method == "POST":
        return render_template("gallery.html")
    else: 
        alt_text = request.args.get("alt_text")
        if alt_text:
            data = solar(alt_text)
            return render_template("info.html", data=data)
        
        return render_template("gallery.html")
    
@app.route("/events")
def events():
    event = event_api()
    return render_template("events.html", event= event)