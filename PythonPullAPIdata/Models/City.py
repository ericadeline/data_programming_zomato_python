# This Model represents one CITY ################################################################################

# City Model
class City:
    #the model contains the following parameters:

    #the object contains the following parameters:
    myCityID = 0        # INT - an ID that is assigned for the city (seqential)
    modified = ""       # STR - the date that the object was created

    cityId = 0          # the city Id given in the JSON object (not seqential)
    name = ""           # the city name
    countryId = 0       # the country ID associated with that city
    countryName = ""    #the country name
    countryFlagUrl = "" #flag URL

    #load the city details    
    def __init__(self, myCityID = 0, modified = "",  cityId = 0, name = "",  countryId = 0, countryName = "", countryFlagUrl = ""):

        self.myCityID = myCityID
        self.modified = modified
        self.cityId = cityId 
        self.name = name 
        self.countryId = countryId 
        self.countryName = countryName 
        self.countryFlagUrl = countryFlagUrl

    #return the city ID
    def getId(self):
        return self.cityId