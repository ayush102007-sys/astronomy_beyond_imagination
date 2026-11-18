from flask import Flask, render_template, request
from API import solar_api as solar , events_api as event_api , images_api as img
from objects_list import view_list

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("base.html")

@app.route("/gallery", methods=["GET","POST"])
def gallery():
    if request.method == "POST":
        return render_template("gallery.html")
    else: 
        gallery_list = view_list
        key = []
        val = []
        img_urls = []
        if gallery_list:
            for ele in gallery_list:
                key.append(next(iter(ele.keys())))
                val.append(next(iter(ele.values())))
        for url in val:
            img_link = img(url)
            img_urls.append(img_link)
            
        return render_template("gallery.html", lst=zip(key, img_urls))
    
@app.route("/events")
def events():
    event = event_api()
    return render_template("events.html", event= event)


    