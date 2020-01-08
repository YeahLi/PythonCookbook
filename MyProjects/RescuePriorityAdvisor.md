# Rescue Priority Advisor
## Introduction:
A cloud application aims to efficiently prioritize rescue effort for all affected cities by a disaster based on the various information feeds.

The rescue priority advisor uses following information to prioritize rescue score:
- Population of the region and city
- Distance to the disaster center
- Distance to the rescue center
- Local weather condition
- Rescue travel time

![](https://git.ng.bluemix.net/henryli/DisasterHelper/raw/master/Picture2.png)

The results are presented on a map including all infromation feeds and rescue score and rank. The color of the tag also indicates the priority level.

## Architecture:
![](https://git.ng.bluemix.net/henryli/DisasterHelper/raw/master/Picture1.png)

## Techniques:
### 1. Frontend:
    a. HTML define the frame of webpage:
		layer 0: headBanner and map (mapbox api)
		layer 1: mySideBar (form, table, ol, button)
		layer 2: A transparent layer to forbid for user interaction with map during calculation. 
		layer 3: coverShow => showing loading gif
	b. CSS decorates the web page. (display, positon, z-index, margin, padding, size)
	c. Javascript:
		Mapbox API: control the GUI of map section.
		Control the interaction events(drag, click, value changed, etc.) with map.
		Send request to backend server and parse the JSON response to show result on the map.

```javascript
map.on('dblclick', function (e) {
	cleanCityMarks();
	coverit();//show loading... view

    var url = "/disasterhelper?lat="+ e.lngLat.toArray()[1] +"&lng=" + e.lngLat.toArray()[0] + "&rescueLat=" + marker.getLngLat().lat + "&rescueLng=" + marker.getLngLat().lng + "&minPopulation=" + minPopulation + "&radius=" + radius;
    sendRequestAndShowResult(url); // query backend server
});

function sendRequestAndShowResult(url) {
    console.log("Request URL is: " + url);
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log("Received response from server!");
            var results = JSON.parse(this.responseText);
            showResults(results); //show marks on map
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

```

### 2. Backend:
	Using Python Flask Framework to implement backend server.
	a. Get data from public REST API:
```python
# Send URL request
import urllib2
import json
def registerUrl(url):
    try:
        data = urllib2.urlopen(url).read()
    except Exception as e:
        print "-----------------------"
        print "Request <" + url + "> failed."
        print e
        print "-----------------------"
    else:
    	return data

populationURL = API_GEODB_URL + "/v1/geo/cities/" + str(cityID)
data = registerUrl(populationURL)
if data is not None:
    dataJson = json.loads(data)
    # Add a new key-pair "population" to the dictionary object city
    city["population"] = dataJson["data"]["population"]
```

	b. Implement the rest api to handle the request from frontend
```python
from flask import Flask
from flask import session
from flask import Response
from flask import request
########################################
# Web Sever Code
########################################
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    #return render_template('index.html')
    return app.send_static_file('index.html')

#http://localhost:5000/disasterhelper?lat=43.38621&lng=-79.83713
@app.route('/disasterhelper', methods=['GET'])
def disasterhelper():
	#1. Collect input args
	latitude = request.args.get('lat', None)
    longitude = request.args.get('lng', None)
    # .......
    #2. Get information from rest api
    resultList = getCitiesAndPopulation(disaterLocation, minPopulation, radius)
    for item in resultList:
    	#add weather and alert atrributes here
        weatherDict = getWeatherNow(item['latitude'], item['longitude'])
        item['weather'] = weatherDict
        alertList = getWeatherAlert(item['latitude'], item['longitude'])
        item['alerts'] = alertList
        #add road distance and time here
        trafficDict = getDistanceAndTime(rescueCenterLat, rescueCenterLng, item['latitude'], item['longitude'])
        item['traffic'] = trafficDict

        #3. Calculate priority from watson
        priority = getPriorityFromWatson(item['population'], weatherAlertSeverity, item['traffic']['travelDurationTraffic'], item['distance'], radius)
        item['priority'] = priority

        #4. Write inputs and results into DB fro future data training
        writeIntoDB(item['population'], weatherAlertSeverity, item['traffic']['travelDurationTraffic'], item['distance'], radius, priority1, priority2)

        #5. sort the list by key
        resultList.sort(reverse=True, key=lambda item: item['priority'])
        i = 1
	    for item in resultList:
	        item['rank'] = i
	        i += 1

	    #6. Return a json file
	    return json.dumps(resultList)

port = os.getenv('PORT', '5000')
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=int(port))    
```
### 3. Waston Machine Learnning
	a. Create a waston stadio on IBM cloud.
	b. Create a training model.
	c. Train the model and generate a model templation.
	d. Publish the template and send rest api request to get the predicted value.

### 4. NoSQL Database -- CloudAnt
```python
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

#Establish a connection to Cloudant DB
client = Cloudant(username, password, url=myurl)
client.connect()

#Create a database
databaseName = "disasterhelper"
myDatabase = client.create_database(databaseName)
if myDatabase.exists():
   print "'{0}' successfully created.\n".format(databaseName)

# Open an existing database
my_database = client['my_database']

# Create documents by using the sample data.
sampleData = [
   [1, "one", "boiling", 100],
   [2, "two", "hot", 40],
   [3, "three", "warm", 20],
   [4, "four", "cold", 10],
   [5, "five", "freezing", 0]
 ]

for document in sampleData:
	jsonDocument = {
		"numberField": document[0],
		"nameField": document[1],
		"descriptionField": document[2],
		"temperatureField": document[3]
	}
	# Create a document by using the database API.
	newDocument = myDatabase.create_document(jsonDocument)
	# Check that the document exists in the database.
	if newDocument.exists():
		print "Document '{0}' successfully created.".format(number)

# Calling an IBM Cloudant API endpoint directly
end_point = '{0}/{1}'.format(myurl, databaseName + "/_all_docs")
params = {
  "selector": {
        "descriptionField" : "warm",
        "temperatureField": 20           
     }        
}
response = client.r_session.get(end_point, params=params)
print "{0}\n".format(response.json())

# Delete DB
try:
    client.delete_database(databaseName)
except CloudantException:
    print "There was a problem deleting '{0}'.\n".format(databaseName)
else:
    print "'{0}' successfully deleted.\n".format(databaseName)

# Close DB
client.disconnect()
```