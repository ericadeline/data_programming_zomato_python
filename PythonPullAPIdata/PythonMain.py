#This python project pulls API data from the Zomato developoers website 
#https://developers.zomato.com/documentation



########################################################################################
#import libraries
########################################################################################

import requests
import urllib3
import json
from FromAPI import *
#from FromSearchAPI import *
#from FromCollectionAPI import *



########################################################################################
#display Display some informational text
########################################################################################

print("****************************************************************************")
print("BDAT1004 Final Assignment - Restaurant Reviews")
print("Created August, 2018")
print("Team members Hui Shi, Saam Chacko, Erica Adeline Aranha, Tran Thi Thu Hieu")
print("Python code by Jennifer Choly")
print("****************************************************************************")
print("\nThis python project pulls API data from the Zomato developers website https://developers.zomato.com/documentation")
print("")


########################################################################################
#set things common to API's 
########################################################################################

apiKey = '2f8b5cf53f104e400683efe3f61dd72e'
apiKeyLabel = 'user-key'
http = urllib3.PoolManager()
base_URL = 'https://developers.zomato.com/api/v2.1'         #this is the base URL string that will be added to in other fuctions to make the specific api string


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)         #disable anoying warning about data security that come up every time the api is called

########################################################################################
# Step 1. First set the CITY NAME
########################################################################################
city_name = 'Toronto'                               #for this demo project, we have only looked at data for Toronto. This could be easily expanded in the future.




########################################################################################
## Step 2. Next find the ---- CITY ID ---- associated with the CITY NAME
# PythonMain.py               
#    --> FromAPI.py    (function FindCityID)
#            --> City.py      (class City)
########################################################################################            

print("\nfinding city ID's for ",city_name)
cityID = FindCityID (apiKey, apiKeyLabel, base_URL, city_name)
print("Using city ID = ", cityID)


########################################################################################
# Step 3. Next we find the ---- COLLECTIONS ---- associated with the CITY ID
# PythonMain.py               
#    --> FromAPI.py 
#        --> CreateCollectionObjects.py
#            --> Collection.py
########################################################################################

print("finding collections for city ID = ", cityID)
outputFromCollection =FromCollectionAPI (cityID, apiKey, apiKeyLabel)
collection_ids = outputFromCollection [0]

print("Found collection_ids",collection_ids, "\n\n")



########################################################################################
# Step 4. find the ---- RESTAURANTS ---- associated with each collection
#PythonMain.py               
#    --> FromAPI.py    (function FromSearchAPI)
#        --> CreateRestaurantObjects.py
#            --> Restaurant.py   (class Resturant)
# and write them in an easiy to parse JSON to a file. This is the file that will be used by C# (this is done in the CreateRestaurantObjects function)
########################################################################################

print("Finding restaurnats ...\n")
count = 0                                                       #count the num of colleciton ID's
start = 0


for collection_id in collection_ids:                            #loop through all the zomato collection id's associated with this city (these id's are not sequential)
    if count == 0:                                              #it's the first collection ID
        flag = 0                                                #flag for the type of separator in the resturant JSON to "[" 
    elif count +1 == len(collection_ids):                       #it's the last collection ID
        flag = -1                                               #flag for the type of separator in the resturant JSON to "]"  
    else:                                                       #it's a middle collection ID
        flag = 1                                                #flag for the type of separator in the resturant JSON to ","  
    
    collection_name = outputFromCollection[1][count].title      #get the collection name asssociated with this collecion ID


    num_res_got_data = 0                                        #initialize the number of restuarant records retrieved from this collection to zero
    num_res_in_collec = 1                                       #initialize the number of restaurants in this collection to 1. assume that there is at least one restaurant in this collection if the colleciton exisits


    while num_res_in_collec != num_res_got_data: 
        # call function to go and make the api call and get the data for the restuants associated with this collection ID
        restaurantByCollection = FromSearchAPI (apiKey, apiKeyLabel, base_URL, cityID, collection_id, collection_name, flag, num_res_got_data)
        num_res_in_collec = restaurantByCollection[0]                           #number of restaurants assocaited with the collection
        num_res_got_data += restaurantByCollection[1]                       #number of restaurants got from the api (sometimes only 20 at a time)

    count +=1                                                   #count one more collection ID
    
print("\ndata conversion complered. \n Please see 'Output/myRestaurantJSON.txt' \n\n")