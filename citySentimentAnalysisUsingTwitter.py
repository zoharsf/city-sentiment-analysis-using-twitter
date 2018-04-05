"""
This project does the following:
--------------------------------
1. Fetch geocode for user provided city name
2. Connect to Twitter and run geo-query
3. Assign a score to each polled tweet using TextBlob
4. Calculate average score for polled tweets
5. Write score and datetime to CSV file
6. Push score to ThingSpeak

In the works for this project:
------------------------------
1. Create DB table for user provided city name
2. Persist polled tweets to created DB table
3. Query tweets and scores from DB according to time frame
4. Visualize score trend
"""

import time

from release.fetchGeoCodeForCity import fetchGeocode
from release.queryTwitterForTweets import *
from release.writeToCsv import *
from release.writeToThingSpeak import *

city = 'New York'

tableName = str.replace(city, " ", "_", )
geocode = fetchGeocode(city)

while True:
    try:
        averageScore = queryTwitterForTweets(geocode)
        print(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + ": " + str(float(averageScore)))
        writeToCsv(tableName, averageScore)
        writeToThingSpeak(averageScore)
    except:
        print("There was a problem fetching data from Twitter.")
    finally:
        time.sleep(60)
