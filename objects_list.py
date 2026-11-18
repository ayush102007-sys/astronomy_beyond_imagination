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
    