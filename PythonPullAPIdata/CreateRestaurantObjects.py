#first, import libraries and models
import requests
import json 
import datetime
from Models.Restaurant import Restaurant
from Functions.Functions import *


########################################################################################
# this function ...
# creates objects for the ---- RESTAURANTS ---- associated with A SINGLE COLLECTION
# This function loops through the resturants in this bit of api data 
# creates an object for each one
#  AND WRITES THAT OBJECT TO one, appended JSON FILE
########################################################################################

def CreateRestaurantObjects(restaurant_data, collection_id, collection_name, starting_point, flag):

    
    restaurants=[]                                     #create an empty array into which the restaurant objects will be saved

    for id in range (len(restaurant_data)):            #loop through all the lines of the restaurant data list (which was created from the JSON object)
        data = restaurant_data[id]                     #get data for this row of the list array (that is, one restaurant on one day)

        # Assign values from the restaurant data to the array of restaurant objects
        temp = Restaurant(
            starting_point + id+1, 
            date_today(),
            collection_id,
            collection_name, 
            data["restaurant"]["R"]["res_id"], 
            data["restaurant"]["name"], 
            data["restaurant"]["location"]["latitude"], 
            data["restaurant"]["location"]["longitude"],  
            data["restaurant"]["cuisines"], 
            data["restaurant"]["average_cost_for_two"], 
            data["restaurant"]["price_range"], 
            data["restaurant"]["user_rating"]["aggregate_rating"], 
            data["restaurant"]["user_rating"]["rating_text"], 
            data["restaurant"]["has_online_delivery"], 
            data["restaurant"]["has_table_booking"])



        restaurants.append(temp)                       #append the array of object instances to include this instance


        ########################################################################################
        ########################################################################################
        #  now we create /append the JSON FILE which will be read from C#
        ########################################################################################
        ########################################################################################

        myRestaurantJSON =""                              #initialize the JSON text to blank. it will be updated below
        fileName = 'Output/myRestaurantJSON.txt'            #set the file name that the JSON will be saved to 

        if flag ==0:
            writeToFile(myRestaurantJSON, fileName)        # Write the Array to a new file as JSON 
            myRestaurantJSON = "[\n" + temp.toJSON() + ",\n"  #then add the JSON text called in the object, and also add a comma
            flag +=1                                        #change the flag
        elif flag ==-1:
            if (id+1) != len(restaurant_data):             #if it's not the last id
                myRestaurantJSON += temp.toJSON() + ",\n"  #then add the JSON text called in the object, and also add a comma
            else:                                       #if it's the last id
                myRestaurantJSON += temp.toJSON() + "]\n"  #then add the JSON text called in the object, and also add a comma
        else:
            myRestaurantJSON += temp.toJSON() + ",\n"  #then add the JSON text called in the object, and also add a comma

        appendFile(myRestaurantJSON, fileName)        # Write the Array to a new file as JSON 
        

    


