from flask import Flask, abort, render_template, request, session
from API import solar_api as solar , events_api as event_api , images_api as img, object_api as objects, wiki 
from objects_list import create_list
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_KEY")

@app.route("/") 
def home():
    return render_template("base.html")

@app.route("/gallery", methods=["GET","POST"])
def gallery():
    if request.method == "POST":
        session["obj"] = ['planet', 0]
        return render_template("gallery.html")
    else:  
        category = request.args.get("cat_text", default= session['obj'][0])
        idx = request.args.get("idx", default= session['obj'][1], type=int)
        key = []
        val = []
        img_urls = []
        gallery_list = create_list(category, idx)
        if gallery_list:
            session['obj'] = [category, idx]
            
            for ele in gallery_list:
                key.append(next(iter(ele.keys())))
                val.append(next(iter(ele.values())))
        for url in val:
            img_link = img(url)
            img_urls.append(img_link)
            
        return render_template("gallery.html", lst=zip(key, img_urls))
    
@app.route("/info")
def info():
    obj = request.args.get("alt_text", "").strip()
    image_url = request.args.get("image_url")
    description = wiki(obj)
    if not obj:
        abort(400, description="An object name is required.")
    
    if obj in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Moon"]:
        solar_data = solar(obj.lower())
        return render_template(
            "info.html",
            solar_data=solar_data,
            description= description,
            object_name=obj,
            image_url=image_url,
        )
        
    else:
        space_data = objects(obj)
        return render_template(
            "info.html",
            space_data=space_data,
            description= description,
            object_name=obj,
            image_url=image_url,
        )
    
@app.route("/events")
def events():
    event = event_api()
    return render_template("events.html", event= event)


    