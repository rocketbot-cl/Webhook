# Webhook
  
Create a Webhook so the robot can listen for a request before continuing; the URL will be '0.0.0.0:port/endpoint.  

*Read this in other languages: [English](Manual_Webhook.md), [Português](Manual_Webhook.pr.md), [Español](Manual_Webhook.es.md)*
  
![banner](imgs/Banner_Webhook.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  

## How to use this module
To use this module, you need to have a port available to expose the webhook.

### Expose the webhook with NGROK (Optional)

1. Download NGROK (https://ngrok.com/download)
2. Unzip the file
3. Run ngrok and run command "ngrok http port-number" Here the port-number is: 5002
Once you run the above command it will expose two URLs. One for HTTP and another for HTTPS. You can use either of them.
4. Copy the public URL of the HTTP and HTTP.

![NGROK](imgs/ngrok.png)

### Use the webhook

When executing the 'Create webhook' command, Rocketbot will pause waiting for the url configured in the command to be queried, either with a GET or POST request. If the request is GET, the data to be sent must be in the URL. If the request is POST, the data must be in the body of the request.

This will return the following JSON:

    {
        "status": "true",
        "uuid": "2c9f8f7e-b8e7-4b5b-b8e7-4b5b8e7b8e7b"
    }


To get data from Rocketbot, you must query the url 
'localhost:port/:enpoint/:uuid'.
This will return a JSON response in the following format:

    {
        "status": True",
        "data": datos_desde_rocketbot
    }


## Description of the commands

### Create webhook
  
With this command you can create an endpoint for the robot to listen to a request before continuing, the url will be '0.0.0.0:port/endpoint'
|Parameters|Description|example|
| --- | --- | --- |
|Endpoint|Endpoint where you need create a request, by default will be '/'|/webhook|
|Port|Port where you need create a webwook, by default will be '5005'|5005|
|Data to return|Data that you want to return when querying the urlport/endpoint/uuid route. This must be an object that contains as key the uuid obtained when querying the endpoint and the value must be what you want to send. See example|{'255de1a0-a6ea-465e-aa6a-0d6b25dd81c6': ['data', 'data2']}|
|Method|Type of method to query the webhook. Can be GET or POST|GET|
|Variable where to store the result|Variable name where to store the result of the query. Example 'resultado'|Variable|
|Get all the data|Selecting this checkbox will give you all the details of the request.|-|
