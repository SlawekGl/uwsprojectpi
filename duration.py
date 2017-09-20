from googlemaps.client import Client
from googlemaps.distance_matrix import distance_matrix

from duration_auth import (
        apiKey
)

gmaps = Client(apiKey)
data = distance_matrix(gmaps, "55.781121, -4.045619", "56.454346, -3.016491")
duration = data['rows'][0]['elements'][0]['duration']['text']
print(duration)
