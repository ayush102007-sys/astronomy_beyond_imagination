from datetime import datetime, timedelta, timezone
import requests, os
from dotenv import load_dotenv
from objects_list import PROPERTY_CONFIG, PROPERTY_LABELS

IST = timezone(timedelta(hours=5, minutes=30), name="IST")
load_dotenv()

def solar_api(planet):
    url = f"https://api.le-systeme-solaire.net/rest/bodies/{planet}"

    API_KEY = os.getenv("SOLAR_API_KEY")

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )
        response.raise_for_status()
        data = response.json() 
        
        # Extract mass
        mass_data = data.get("mass") or {}

        mass_value = mass_data.get("massValue")
        mass_exponent = mass_data.get("massExponent")

        mass = None
        moons_list = []
        moon_dict = {}
        moons = data.get("moons", [])
        if planet not in ["venus", "mercury", "moon", "sun"]:
            for moon in moons:
                moon_name = moon.get("moon")
                if moon_name:
                    moons_list.append(moon_name)
                moon_dict["total"] = len(moons_list)
                moon_dict["moons"] = moons_list
                
        else:
            moon_dict["total"] = 0
            
        if mass_value is not None and mass_exponent is not None:
            mass = mass_value * (10 ** mass_exponent)

        planet_data = f"{planet}_info"
        # Extract other properties
        planet_data = {
        "name": data.get("englishName"),
        "mass_kg": mass,
        "rotation_period_hours": data.get("sideralRotation"),
        "orbital_period_days": data.get("sideralOrbit"),
        "distance_from_sun_km": data.get("semimajorAxis"),
        "moons": moon_dict['total']
        }

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    return planet_data

def object_api(obj):
    url = "https://spacecatalog.org/api/v1/search"

    try:
        params = {
            "q": f"{obj}",
            "limit": 1
        }
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        data = response.json()

        if not data.get("results"):
            return {}

        first_result = data["results"][0]
        category = first_result.get("category")
        cat_lst = PROPERTY_CONFIG.get(category, [])
        selected_values = {}

        for key in cat_lst:
            value = f"{first_result.get(key):.2f}" if type(first_result.get(key)) == float else first_result.get(key)

            if value is not None:
                details = PROPERTY_LABELS.get(key, {})

                label = details.get("label", key)
                unit = details.get("unit", "")

                formatted_value = f"{value} {unit}".strip()

                selected_values[label] = formatted_value

        return selected_values

    except requests.exceptions.RequestException as error:
        print("API request failed:", error)
        raise



def events_api():
    url = "https://spacecatalog.org/api/v1/events"

    try:
        params = {
        "limit": 6
    }
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
        data = response.json()
        
        event_list = data['events']
        events_lst = []
        for event in event_list:
            time_utc = datetime.fromisoformat(
                event["time"].replace("Z", "+00:00")
            )
            events_lst.append({
                "title": event.get("title"),
                "description": event.get("description"),
                "kind": event.get("kind"),
                "time_date": time_utc.astimezone(IST).strftime(
                    "%Y-%m-%d %H:%M:%S IST"
                ),
                "event_url": event.get("url"),
            })
    
    except requests.exceptions.RequestException as error:
        print("API request failed:", error)

    return events_lst

def images_api(nasa_id):
    
    url = f"https://images-api.nasa.gov/asset/{nasa_id}"

    response = requests.get(url, timeout=40)
    response.raise_for_status()

    data = response.json()

    image_files = [
        item["href"]
        for item in data["collection"]["items"]
        if item["href"].lower().endswith((".jpg", ".jpeg", ".png", ".tif", ".tiff"))
    ]

    # Prefer original resolution; otherwise use medium resolution
    image_url = next(
        (url for url in image_files if "~orig." in url),
        next((url for url in image_files if "~medium." in url), None)
    )

    return image_url