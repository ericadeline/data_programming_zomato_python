#first, import libraries and models
import requests
import json 
import datetime
from Models.Collection import Collection
from Functions.Functions import *


########################################################################################
# this function ...
# creates objects for the ---- COLLECTIONS ---- associated with A SINGLE CITY
# This function loops through the collections in this city
# creates an object for each one
#  AND WRITES THAT OBJECT TO one, appended JSON FILE
########################################################################################


def CreateCollectionObjects(collection_data):

    print("converting Collection JSON to python objects ...\n")  #provide status update

    collections=[]                                     #create an empty array into which the collection objects will be saved
    myCollectionJSON = "[\n"                           #create a string that will be populated with the new JSON objects
    collection_ids = []                           #create an empty array into which the collection ID's will be saved

    for id in range (len(collection_data)):            #loop through all the lines of the collection data list (which was created from the JSON object)
        data = collection_data[id]                     #get data for this row of the list array (that is, one collection on one day)

        collection_ids.append(data["collection"]["collection_id"])  #add the next collection ID to the list of collection id's

        # Assign values from the collection data to the array of Collection objects
        temp = Collection(
            id+1, 
            date_today(), 
            data["collection"]["collection_id"], 
            data["collection"]["image_url"], 
            data["collection"]["res_count"], 
            data["collection"]["title"], 
            data["collection"]["description"])


        collections.append(temp)                       #append the array of object instances to include this instance
        if (id+1) != len(collection_data):             #if it's not the last id
            myCollectionJSON += temp.toJSON() + ",\n"  #then add the JSON text called in the object, and also add a comma
        else:                                       #if it's the last id
            myCollectionJSON += temp.toJSON() + "\n]"  #then the last element should be a closed bracket

        #if id < 10:                                #for the first ten lines
        #    print(temp.__str__())                   #print the descriptive object string    
    

    writeToFile(myCollectionJSON,'Output/myCollectionJSON.txt')        # Write the Array to a new file as JSON 

    return collection_ids, collections       #return the list of colleciton ID's


