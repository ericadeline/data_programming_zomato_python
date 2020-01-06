# Resturant Model
# This Model represents one entity in the Restaurants data source ################################################################################

#import libraries
import requests
import json 


# Restaurant Model
class Restaurant(object):

    #-----------------------------------------------------------------------------
    #the model contains the following parameters:
    myRestaurantID = 0      #     myRestaurantID         INT - an ID that is assigned for the Restaurant (seqential)
    modified = ""           #     modified               STR - the date that the object was created

    #this parameter was passed from the collection object
    collection_id = 0       #    COLLECITON ID           INT - the colleciton ID given in collection API (not seqential)
    collection_name = ""    #    collection name        STR - the name of the collection associated with this collection id

    # only some of the parameters were pulled from the api 
    #The following properties are derived from the source JSON file 
    res_id = 1111           #   restaurant ID           INT - the restaurant ID given in the restaurant API (not sequntial)
    name = "aaa"            #   restaurnat name         STR
    latitude = ""           #   latitude               
    longitude = ""          #   longitude
    cuisines = ""           #       cuisines 
    average_cost_for_two = ""   #    average cost for two people
    price_range = ""            # price range
    aggregate_rating = ""       #aggreagate rating 
    rating_text = ""            #rating text
    has_online_delivery = ""        #does it have online deliveries? 
    has_table_booking = ""          #does it have table bookings? 

    #-----------------------------------------------------------------------------
    #the object also contains the following :
    #__init__
    # __str__       creates a string to describe the object instance
    # toJSON        converts python object to a JSON object 


    # Constructor with Default Parameters, allows for Parameterless Instance
    def __init__(self, myRestaurantID = 0, modified = "", collection_id = 0, collection_name = "",  res_id = 1111, name = "aaa", latitude = "", longitude = "", cuisines = "", average_cost_for_two = "", price_range = "", aggregate_rating = "", rating_text = "", has_online_delivery = "", has_table_booking = ""):
        self.myRestaurantID = myRestaurantID 
        self.modified = modified 
        self.collection_id = collection_id
        self.collection_name = collection_name
        self.res_id = res_id
        self.name = name 
        self.latitude = latitude 
        self.longitude =     longitude 
        self.cuisines =     cuisines 
        self.average_cost_for_two =     average_cost_for_two 
        self.price_range =     price_range 
        self.aggregate_rating =     aggregate_rating 
        self.rating_text =     rating_text 
        self.has_online_delivery =     has_online_delivery 
        self.has_table_booking =     has_table_booking 


    # String representation of this Model
    def __str__(self):
        output = "Data read on " + str(self.modified) + \
            ": " + type(self).__name__ + \
            " ID" + str(self.myRestaurantID) + \
            ". belongs to collecion num" + str(self.collection_id) + \
            ". API restaurant ID " + str(self.res_id) + \
            ", " + str(self.name)
        
        #return the string we created
        return output                                                  

#method that conversts this instance to JSON
    def toJSON(self):
        #use the dumps method in the json library to convert it to JSON in one neat line :)
        oneJSONitem = json.dumps(self, default=lambda o: o.__dict__)    
        #return the JSON string
        return oneJSONitem  