# This Model (Object) represents one entity in the Collections data source ################################################################################

#import libraries
import requests
import json 


# Collection Model
class Collection(object):

    #-----------------------------------------------------------------------------
    #the model contains the following parameters:
    myCollectionID = 0      # Param 1    myCollectionID         INT - an ID that is assigned for the collection (seqential)
    modified = ""           # Param 2    modified               STR - the date that the object was created

    #The following properties are derived from the source JSON file 
    collection_id = 0       # Param 3   COLLECITON ID           INT - the ID given in the JSON object (not seqential)
    image_url = ""          # Param 4   IMAGE URL               STR
    res_count = 0           # Param 5   RESTAURANT COUNT        INT
    title = ""              # Param 6   TITLE                   STR
    description = ""        # Param 7   DESCRIPTION             STR

    #-----------------------------------------------------------------------------
    #the object also contains the following :
    #__init__
    # __str__       creates a string to describe the object instance
    # toJSON        converts python object to a JSON object 


    # Constructor with Default Parameters, allows for Parameterless Instance
    def __init__(self, myCollectionID = 0,  modified = "", collection_id = 0, image_url = "", res_count = 0, title = "", description = ""):
        self.myCollectionID = myCollectionID 
        self.modified = modified 
        self.collection_id = collection_id
        self.image_url = image_url 
        self.res_count = res_count
        self.title = title 
        self.description = description


    # String representation of this Model
    def __str__(self):
        output = "Data read on " + str(self.modified) + \
            ": " + type(self).__name__ + \
            " ID" + str(self.myCollectionID) + \
            ". API collection ID " + str(self.collection_id) + \
            ", " + str(self.description)
        #return the string we created
        return output                                                  

#method that conversts this instance to JSON
    def toJSON(self):
        #use the dumps method in the json library to convert it to JSON in one neat line :)
        oneJSONitem = json.dumps(self, default=lambda o: o.__dict__)    
        #return the JSON string
        return oneJSONitem