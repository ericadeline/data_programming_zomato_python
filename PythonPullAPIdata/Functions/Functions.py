import datetime
import json
from Models.City import *

#function date_today returns today's date
def date_today ():
    now = datetime.datetime.now()
    return (str(now).split(' ')[0])      #Return today's date. I got this code from here https://stackoverflow.com/questions/17053099/how-to-print-current-date-on-python3


#function writeToFile writes to a file
def writeToFile(stringVar,fileName):
	with open(fileName, 'w') as f:     #write a new file
#	with open('Data/Restaurants.txt', 'a') as f:     #append the file
		f.write(stringVar)
		f.write('\n')
		f.close()

#function append file
def appendFile(stringVar,fileName):
	with open(fileName, 'a') as f:     #write a new file
		f.write(stringVar)
		f.write('\n')
		f.close()


