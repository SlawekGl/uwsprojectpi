import requests
import json
import simplejson
from requests.auth import HTTPBasicAuth

from get_flights_arrival_est_time_auth import (
        apiKey
)

username = "UWSProjectPi"
fxmlUrl = "https://flightxml.flightaware.com/json/FlightXML3/"

#flightno = input("Please type your flight number: ")
payload = {'ident': 'DAL85', 'howMany':'1'}
response = requests.get(fxmlUrl + "FlightInfoStatus", params=payload, auth=(username, apiKey))

if response.status_code == 200:
    decodedResponse = response.json()
    for flight in decodedResponse['FlightInfoStatusResult']['flights']:
        print "Flight number {} from {} - airport: {} to {} - airport: {} is expected to land at {} {}.".format(flight['ident'], flight['origin']['city'], flight['origin']['airport_name'], flight['destination']['city'], flight['destination']['airport_name'], flight['estimated_arrival_time']['time'], flight['estimated_arrival_time']['tz'])
else:
    print "There was an error retrieving the data from the server."
