# Samrt Track
## Introduction

SmartTrack Case viewer:
This web application uses a salesforce license to make SalesForce API calls on behalf of a registered user.

Smart Track:
Analyze aged cases with its RTC tickets, find out where the case pending on.

## Architect

1. Salesforce Adapter(NodeJS) to retrieve case information from salesforce database.

2. SmartTrack(JavaEE) to receive the data and using Spark to analyze it.

3. Javascript parse the returned json data and show it on the web page

## Techniques

### 1. NodeJS framework
	1.) Install NodeJS.
	2.) In your terminal, navigate to the root folder of this repository and run command ```npm install```
	Since the package.json in the web app includes all the dependencies necessary
	3.) In your terminal, run app.js to deploy the system ```node app.js```
	This should run the app and set up the server accordingly. 

**app.js:**
```javascript
/* Preparation */
var express = require('express');
// cfenv provides access to your Cloud Foundry environment
// for more info, see: https://www.npmjs.com/package/cfenv
var cfenv = require('cfenv');
// get the app environment from Cloud Foundry
var appEnv = cfenv.getAppEnv();
// create a new express server
var app = express();
// make the JSON print pretty
app.set('json spaces', 4);
app.use(express.static(__dirname + '/public'));

/* Rest API Server 
  Routes for /api 
  Handlers are in /routes/api/*
  These routes are authenticated.
*/
var sfCase = require('./routes/api/case.js');

/* Map REST API to related function */
app.get('/api/case/:id', sfCase.read);
app.get('/api/case.full/:id', sfCase.readFull);
app.get('/api/caseEvents/:id', sfCase.readEvents);
app.get('/api/isClient/:id', sfCase.isClient);

/* Start Server */
//Starting server in 3000 port for bluemix
if (process.env.VCAP_APPLICATION) {
    // if Bluemix start server on the specified port and binding host
	app.listen(appEnv.port, '0.0.0.0', function() {
	  // print a message when the server starts listening
	  console.log("server starting on " + appEnv.url);
	});
} else {
    var port = 3000;
    // start server on the specified port and binding host
	app.listen(port, '0.0.0.0', function() {
        // print a message when the server starts listening
        console.log("server starting local on " + port);
      }); 
}
```

**./routes/api/case.js**
```javascript
//REST API /api/case/<Case Number>
exports.read = function(req, res) {
	/* 1. Using Salesforce API to logon */
	var POST = require('../../lib/sfAPI');
	//getTokenPromise will make the program wait to get the token from getToken() before moving onto getting the account list
	var getTokenPromise = POST.getToken();
	//Won't run until getToken returns, anything not in this .then block can be run however
	getTokenPromise.then(function(token){
		//Selects the access token from the json
		var accessToken = token.obj["access_token"];
		
		/* 2. Get case info by ID */
		//Create a new promise to get the case info from SF
		var getCasePromise = POST.getCase(accessToken, req.params.id);//added functionality to getCase
		
		//Won't run until getAccountsByName returns case
		getCasePromise.then(function(caseObj){
			//If the case doesn't exist, return a null
			if(caseObj.statusCode != 200){
				console.log("case is null ")
				res.json({
					case_:	caseObj.obj,
					statusCode:	caseObj.statusCode,
					statusMessage: caseObj.statusMessage
					
				});
			}
			else{
				//3. Return json object as response. 
				console.log(caseObj);
				res.json({
					pmrNumber: caseObj.obj.CaseNumber,
					priority: caseObj.obj.Priority,
					//........
				});
			}
		}, function(err){
			console.log(err);
		});
	}, function(err){
		console.log(err);
	});
};
```

### 2. JavaEE Serverlet framework
	a. Frontend: index.html
```javascript
 $("#PMR_Num_Btn").click(function(){
	  var queryURL = "./api/query";	  
	  
	  if ($("#PMR_Num").val() == "") {
		  alert("Please specify a Case number.");
		  return;
	  }

	  $('#loading-image').show();
	  
      /* AJAX based Jersey Web Service Call */ 
	  $.post(queryURL, $("#queryForm").serialize(), 
	  	function (data) {
	  		$('#loading-image').hide();
			$("#info").empty();
			$("#visualization").empty();
			$("#info").append("<tr><td align=right><font color=Blue>Case:</font></td><td>"+ data.PMR_Num +"</td></tr>");
		});
	}
)
```
	
	b. Serverlet: web.xml
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" id="WebApp_ID" version="2.5">
  <display-name>PMR SmartTrack Service</display-name>
  <welcome-file-list>
    <welcome-file>index.html</welcome-file>
  </welcome-file-list>
  
  <servlet>
    <servlet-name>Jersey REST Service</servlet-name>
    <servlet-class>com.sun.jersey.spi.container.servlet.ServletContainer</servlet-class>
    <init-param>
      <param-name>com.sun.jersey.config.property.packages</param-name>
      <param-value>com.ibm.platform.support.pmranalyzer.resources</param-value>
    </init-param>
    <init-param>
        <param-name>com.sun.jersey.api.json.POJOMappingFeature</param-name>
        <param-value>true</param-value>
    </init-param>
    <load-on-startup>1</load-on-startup>
  </servlet>
  
  <servlet-mapping>
    <servlet-name>Jersey REST Service</servlet-name>
    <url-pattern>/api/*</url-pattern>
  </servlet-mapping>
  
</web-app>
``` 
	
	c. REST API code: SmartTrackWebService.java
```java
package com.ibm.platform.support.pmranalyzer.resources;
import org.json.JSONArray;
import org.json.JSONObject;

@Path("/query")
public class SmartTrackWebService {
	//@Path("/query")
	@POST
	@Consumes(MediaType.APPLICATION_FORM_URLENCODED)
    @Produces(MediaType.APPLICATION_JSON)
    public Response getPMREvents(@FormParam("PMR_Num") String pmr,
    		                     @FormParam("pmrEventType") String pmrEventType,
    		                     @FormParam("groupType") List <String> groupType,
    		                     @FormParam("iconOnly") String iconOnly,
    		                     @FormParam("RTC_Defect_Num") String rtc_defect,
    		                     @FormParam("RTC_Build_Num") String rtc_build,
    		                     @FormParam("RTC_Support_Num") String rtc_support) 
    {	
        System.out.println("PMR number="+pmr+";rtc defect number="+ rtc_defect + ";rtc build number=" + rtc_build);
        //......
        JSONObject pmrJSON =  new JSONObject();
        pmrJSON.put("PMR_Num", pmrInfo.getPmrNumber());

        loadPmrLifeCycle(PmrTrackOpt pmropt)
        //......
        loadRtcLifeCycle(String rtcIdStr, String pmr)

        //Return json data
        return Response.ok(pmrJSON.toString()).build();
    }
}
```

### 3. Spark framework
```java
/* Load all PMR information into a Spark dataframe */
SparkConf sparkConf = new SparkConf().setAppName("pmrEventSql").setMaster("local");
JavaSparkContext ctx = new JavaSparkContext(sparkConf);
sqlContext = new SQLContext(ctx);

/* Get PMR Event list */
// Load PMR basic information
PmrInfo pInfo= loadPmrInfo(pmropt.getPmrStr());
//Get PMR Event list
JSONArray pmrData = getPmrData(pmropt.getPmrStr(),pInfo);

/* Load PMR Event data pmrData */
List<String> jsonData = Arrays.asList(pmrData.toString());		
JavaRDD<String> pmrEventRDD = ctx.parallelize(jsonData);
DataFrame pmrEventFromJson = sqlContext.read().json(pmrEventRDD.rdd());
//show data in dataframe
pmrEventFromJson.show();  	
pmrEventFromJson.registerTempTable("PMREvent");
```