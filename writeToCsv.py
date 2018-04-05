import datetime
import csv

import os


def writeToCsv(tableName, averageScore):
    fileName = tableName + '_ScoreByDateTime.csv'
    if os.path.exists(fileName):
        with open(fileName, 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow((datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"), averageScore))
    else:
        with open(fileName, 'w', newline='') as csvfile:
            csvWriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerow(['DateTime', 'Score'])
            csvWriter.writerow((datetime.datetime.now().strftime("%Y-%m-%d-%H-%M"), averageScore))
