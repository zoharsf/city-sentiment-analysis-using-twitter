import urllib.parse
import urllib.request
from release.credentials import apiKey
from tweepy.streaming import json


# https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY
def fetchGeocode(city):
    data = {}
    data['address'] = city
    url_values = urllib.parse.urlencode(data)
    print(url_values)
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    full_url = url + '?' + url_values + '&key=' + apiKey
    data = urllib.request.urlopen(full_url)
    response = json.load(data)
    print(response)
    latitude = response['results'][0]['geometry']['location']['lat']
    print('lat: ', latitude)
    longitude = response['results'][0]['geometry']['location']['lng']
    print('lng: ', longitude)
    radiusInKm = 20
    geocode = str(float(latitude)) + ',' + str(float(longitude)) + ',' + str(float(radiusInKm)) + 'km'
    print(geocode)
    return geocode
