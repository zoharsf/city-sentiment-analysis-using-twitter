from release.credentials import thingSpeakWriteApiKey

import urllib.parse
import urllib.request


def writeToThingSpeak(averageScore):
    data = {}
    data['field1'] = averageScore
    url_values = urllib.parse.urlencode(data)
    fullURL = 'http://api.thingspeak.com/update?api_key=' + thingSpeakWriteApiKey + '&' + url_values
    urllib.request.urlopen(fullURL)
