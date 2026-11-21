import random
object_dict = [ 
    {"planet": 
    [{"Mercury": "PIA15161"},
    {"Venus": "PIA00271"},
    {"Earth": "PIA18033"},
    {"Mars": "PIA03276"},
    {"Jupiter": "hubble-captures-vivid-auroras-in-jupiters-atmosphere_28000029525_o"},
    {"Saturn": "PIA05982"},
    {"Uranus": "PIA18182"},
    {"Neptune": "PIA01492"}]},
    
    {"star":
    [{"Sun": "PIA26681"},
    {"Proxima Centauri": "GSFC_20171208_Archive_e000214"},
    {"T Tauri": "hubble-sees-a-young-star-take-center-stage_16708377846_o"},
    {"RS Puppis": "GSFC_20171208_Archive_e001283"},
    {"Fomalhaut": "PIA15425"},
    {"Betelguese": "PIA16680"},
    {"Vega": "PIA07218"},
    {"Altair": "PIA04204"}
    ]},
    
    {"galaxy":
    [{"Andromeda": "7993119"},
    {"Whirlpool": "PIA23005"},
    {"Sombrero": "PIA15226"},
    {"Pinwheel": "GSFC_20171208_Archive_e001979"},
    {"Triangulum": "GSFC_20171208_Archive_e001913"},
    {"Cigar": "PIA23010"},
    {"M81": "PIA09579"},
    {"M87": "PIA23122"},
    {"Sunflower": "PIA13900"},
    {"NGC 300": "PIA10113"}
    ]},
    
    {"nebulae":
    [{"Orion" : "PIA08654"},
    {"Pillars of Creation": "GSFC_20171208_Archive_e000842"},
    {"Crab Nebula": "PIA03606"},
    {"Ring Nebula": "hubble-sees-a-dying-stars-final-moments_20149292766_o"},
    {"Helix Nebula": "PIA18164"},
    {"Carina Nebula": "PIA17257"},
    {"Lagoon Nebula": "PIA14728"},
    {"Trifid Nebula": "PIA17834"},
    {"Horsehead Nebula": "GSFC_20171208_Archive_e001518"},
    {"Rosette Nebula": "PIA09268"},
    {"Cat's Eye Nebula": "GSFC_20171208_Archive_e002155"},
    {"Dumbbell Nebula": "PIA14417"},
    {"Bubble Nebula": "GSFC_20171208_Archive_e000383"}

    ]}   
]
def create_list(obj_cat, index):
# Select six distinct elements at random.
    view_list = random.sample((object_dict[index].get(f'{obj_cat}', [])) , 6)
    
    return view_list

# Property Config

PROPERTY_CONFIG = {

    "star": [
        "name",
        "constellation",
        "dec_deg",
        "ra_deg",
        "radius_solar",
        "distance_ly",
        "mass_kg",
        "mag",
        "mag_band",
        "object_type",
    ],

    "galaxy": [
        "name",
        "constellation",
        "dec_deg",
        "ra_deg",
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
        "ra_deg",
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
