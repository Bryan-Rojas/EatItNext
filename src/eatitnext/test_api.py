import requests
import json
from .secret_settings import edamam_api_key, edamam_app_id

"""
import requests

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url, params=params)
data = resp.json() # Check the JSON Response Content documentation below
"""

URL = 'https://api.edamam.com/api/food-database/parser?nutrition-type=logging&ingr=red%20apple&app_id={your app_id}&app_key={}'