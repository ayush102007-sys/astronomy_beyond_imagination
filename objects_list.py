import random
object_dict = [
    {"Mercury": "PIA15161"},
    {"Venus": "PIA00271"},
    {"Earth": "PIA18033"},
    {"Mars": "PIA03276"},
    {"Jupiter": "hubble-captures-vivid-auroras-in-jupiters-atmosphere_28000029525_o"},
    {"Saturn": "PIA05982"},
    {"Uranus": "PIA18182"},
    {"Neptune": "PIA01492"}
]

# Select six distinct elements at random.
view_list = random.sample(object_dict, 6)

key = []
val = []
for ele in view_list:
    key.append(next(iter(ele.keys())))
    val = next(iter(ele.values()))
    
    
# Property Config

PROPERTY_CONFIG = {

    "star": [
        "name",
        "constellation",
        "dec_deg",
        "ra_deg"
        "radius_solar",
        "distance_ly",
        "mass_kg",
        "mag",
        "mag_band"
        "object_type",
    ],

    "galaxy": [
        "name",
        "constellation",
        "dec_deg",
        "ra_deg"
        "discovered",
        "distance_ly",
        "mag",
        "mag_band",
        "object_type",
        "slug"
    ],

    "nebula": [
        "name",
        "constellation",
        "dec_deg",
        "ra_deg"
        "discovered",
        "distance_ly",
        "mag",
        "mag_band",
        "object_type",
        "slug"
    ]
}    

PROPERTY_LABELS = {
    "surface_temperature_k": {
        "label": "Surface Temperature",
        "unit": "K"
    },

    "mass_solar": {
        "label": "Mass",
        "unit": "Solar masses"
    },

    "radius_solar": {
        "label": "Radius",
        "unit": "Solar radii"
    },

    "luminosity_solar": {
        "label": "Luminosity",
        "unit": "Solar luminosities"
    },

    "distance_ly": {
        "label": "Distance",
        "unit": "light-years"
    },

    "mag": {
        "label": "Apparent Magnitude",
        "unit": ""
    },

    "redshift": {
        "label": "Redshift",
        "unit": ""
    },

    "orbital_period_days": {
        "label": "Orbital Period",
        "unit": "days"
    },
    
    "dec_deg": {
        "label": "Declaration",
        "unit": "°"
    },
    "ra_deg": {
        "label": "Right Ascension",
        "unit": "°"
    }
}
