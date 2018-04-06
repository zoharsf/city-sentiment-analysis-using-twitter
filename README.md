# city-sentiment-analysis-using-twitter
A Python project which analyzes twitter data from any user-provided city

![Sentiment scores for Tel Aviv](graph.PNG?raw=true "Sentiment scores for Tel Aviv")

Project overview
--------------------------------
1. Fetch the geocode for the user-provided city name using a Google API
2. Connect to Twitter and run a geo-query using the Tweepy library
3. Assign a score to each polled tweet using the TextBlob library
4. Calculate the average sentiment score for all polled tweets
5. Write score as well as the current Datetime to a local CSV file
6. Publish score to ThingSpeak

Instructions
------------
1. Edit the value of the "city" property in the citySentimentAnalysisUsingTwitter.py file to whichever city you would like to analyze. The fetchGeocode(city) method will fetch the geocode for the desired city using a Google API
2. Populate all the values of the properties in the credentials.py file (each property name is indicative of its purpose)
3. Edit the time to sleep (in seconds) in citySentimentAnalysisUsingTwitter.py if you wish to poll Twitter in a different interval
4. Run the citySentimentAnalysisUsingTwitter.py using Python 3.6 (preferably)

Future plans for this project
------------------------------
1. Create a DB table for each user-provided city name
2. Persist all of the polled tweets and their respective sentiment score to the relevant DB table
3. Query tweets and scores from relevant DB table according to a predefined time frame
4. Visualize score trend locally

Notes
-----
1. The sentiment score is on a scale of (-1) to 1. (-1) being least positive, 1 being most positive
2. The CSV filename is automatically generated according to the user-provided city name and is in the following structure: <city_name>_ScoreByDateTime.csv
3. Tweets are gathered inside a 20km radius from the user-provided city
4. The choice to visualize the information gathered in this project using ThingSpeak was arbitrary. There are many other services which provide similar visualization options which I hope to try out in future projects
