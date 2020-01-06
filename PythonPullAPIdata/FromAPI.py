#FUNCTIONS THAT CALL API'S

#Import things
import requests
import urllib3
import json
import datetime

from Models.City import *
from CreateRestaurantObjects import*
from CreateCollectionObjects import *

from Functions.MakeQueryStrings import *
from Functions.Functions import *
http = urllib3.PoolManager()



########################################################################################
#------find the CITY ID from the API -------------
# This function builds an API string based on the city name.
# It then returns the cityID associated with that name
########################################################################################            

def FindCityID(apiKey, apiKeyLabel, baseUrl, city_name):
    
    #set specific API string components
    endPoint = '/cities'
    queryParams = ['q']
    values = [city_name]
    queryStr = makeQueryStr(queryParams, values)

    #combine components to make specific API string
    apiStr = baseUrl + endPoint + queryStr                                  #build the API string
    r = http.request('GET', apiStr, headers = {apiKeyLabel: apiKey})        #call the API
    data = (json.loads((r.data).decode('utf-8')))           #load the API data
    locationSuggestions = data.get('location_suggestions')
    if len(locationSuggestions) > 1:
        print('More than one city found! Returning the first city, that is')

    locationSuggestion = locationSuggestions[0]
    print(locationSuggestion.get('name'), ", ", locationSuggestion.get('country_name'))

    city = City(
        1,
        date_today(),
        locationSuggestion.get('id'),  #cityId 
        locationSuggestion.get('name'),     #name
        locationSuggestion.get('country_id'),    #country id
        locationSuggestion.get('country_name'),     #country name
        locationSuggestion.get('country_flag_url'))
    

    return city.getId()                                                     #return the city ID



########################################################################################
# find the ---- COLLECTIONS ---- from the API
# This function builds an API string 
# to call the zomato /collections api
# based on the city ID.
# It then returns the associated collection ID's 
########################################################################################
 
def FromCollectionAPI (cityID, apiKey, apiKeyLabel):

    apiStr = "https://developers.zomato.com/api/v2.1/collections?city_id=" + str(cityID)            #build the API string
    r = http.request('GET', apiStr, headers = {apiKeyLabel: apiKey})                                #access the API data
    apidata = json.loads((r.data).decode('utf-8'))                                                  #load the data
        
    #write the RAW api data to a file (this is for future reference. other formatted JSON will happen when the objects are created)
    filePath = 'Output/RawData/Raw_API_collections_Data_For_City=' + str(cityID) + 'date'+ date_today () +'.txt'        #construct the file path specific to this 
    writeToFile(json.dumps(apidata),filePath)                                                                           #write raw data to a file for reference

    #call some functions to manipulate the collection data to give me a JSON object that can be sent to C# and also a list of collection id's
    collection_data = apidata.get('collections')                    
    collection_ids = CreateCollectionObjects(collection_data)     #create the collection objects. JSON file gets created in these functions. A list of collection ID's is returned

    return collection_ids           #return the list of collection id's



########################################################################################
# find the ---- RESTAURANTS ---- associated with each collection
# This function builds an API string 
# to call the zomato /search api 
# based on the cityID and collectionID.
# It then returns the associated restaurants
########################################################################################

def FromSearchAPI (apiKey, apiKeyLabel, baseUrl, cityId, collection_id, collection_name, flag, starting_point):

    #----------------------------------------------------------------------------------
    #first, construct the api string 
    #    apiStr = baseUrl (passed in when function called) 
    #               + endPoint (set below) 
    #               + queryStr (made of queryParams & Values)
    endPoint = '/search'                        #this is used to make the api string
    queryParams = [                             #these are used to make the api string
        'entity_id',
        'entity_type',
    #        'q',
        'start',
    #        'flag',
    #        'lat',
    #        'lon',
    #        'radius',
    #        'cuisines',
    #        'establishment_type',
        'collection_id',
    #        'category',
        'sort'
    #        'order'
    ]
    values = [                              #these are also used to make the api string. note only some valuse were used
        str(cityId),        #locationID
        'city',             #location type (blank, city, subzone, zone, landmark, metro, group)
    #   'rating',           #value for q
    #   "",                 #value for q
        str(starting_point),   #value for start
    #   "",                 #value for count
    #   "",                 #value for latitude
    #   "",                 #value for longitude
    #   "",                 #value for radius
    #   "",                 #value for cusines
    #   "",                 #value for establishment type
        str(collection_id), #value for collection_id
    #   "",                 #value for category
        ''                  #,         #value for sort (blank, cost, rating, real_distance)
    #   ''                  #value for order (blank, asc, dsc)]
        ]
    queryStr = makeQueryStr(queryParams, values)            #construct the query string
    #----------------------------------------------------------------------------------
    apiStr = baseUrl + endPoint + queryStr                      #assemble the api URL string
    #----------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------
    #NOW WE CAN ACCESS THE DATA ASSOCAITED WITH THAT API STRING

    r = http.request('GET', apiStr, headers = {apiKeyLabel: apiKey})        #access the api data
    apidata = json.loads((r.data).decode('utf-8'))                          #load the data
    restaurants_found = apidata .get('results_found')                       #number of restaurants assocaited with the collection
    restaurants_shown = apidata .get('results_shown')                       #number of restaurants got from the api (sometimes only 20 at a time)

    restaurant_data = apidata.get('restaurants')                            #get the data about the individual restaurants

    #write the RAW api data to a file (this is for future reference. other formatted JSON will happen when the objects are created)
    filePath = 'Output/RawData/Raw_API_City=' + str(cityId) +'CollectionID=' + str(collection_id) + 'date'+ date_today () + 'records '+ str(starting_point+1) + " to " + str(starting_point + restaurants_shown) + '.txt'           #construct the file path specific to this 
    writeToFile(json.dumps(apidata),filePath)                                                                                               #write raw data to a file for reference

    print("creating JSON for collection ID ", collection_id, ", resturant records ", str(starting_point+1), " to ", str(starting_point + restaurants_shown))  #provide status update

    CreateRestaurantObjects(restaurant_data, collection_id, collection_name, starting_point, flag)          #CALL THE FUNCTION to create the restaurnat objects. This is where the JSON that C# calls is created


    return restaurants_found, restaurants_shown







