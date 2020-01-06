
#function to join the parameter/value cobos together. used for making API url
def makeQueryStr(queryParams, values):
	if len(queryParams) == 0:
		return ''
	queryStr = ''
	for param in queryParams:
		i = queryParams.index(param)
		queryStr = queryStr + makeQueryParam(i, param, values[i])
	return queryStr



#function to join a parameter and value together. used for making API url
def makeQueryParam(i, param, value):
	return getQueryStrDelimiter(i) + param + '=' + value;


#function to set the query deliminaer. used for making API url
def getQueryStrDelimiter(index): 
	if index == 0:
		return '?'
	return '&'
