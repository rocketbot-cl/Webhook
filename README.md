
# Webhook
  
With this module you can work with webhook in Rocketbot, how to wait for a request before continuing with the flow of 
your robot  

## Howto install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



### How to use this module

## #How to use this module
  
To use this module, you need to have a port available to expose the webhook.  

### #Expose the webhook with NGROK

## ##Expose the webhook with NGROK
  
  
1. Download NGROK (https://ngrok.com/download)  
2. Unzip the file  
3. Run ngrok and run command "ngrok http port-number" Here the port-number is: 5002  
Once you run the above command it will expose two URLs. One for HTTP and another for HTTPS. You can use either of them.  
4. Copy the public URL of the HTTP and HTTP.  
  
![NGROK](imgs/ngrok.png)  
  

## Overview


1. Create webhook  
With this command you can create an endpoint for the robot to listen to a request before continuing, the url will be 
'0.0.0.0:port/endpoint'

----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**flask**](https://pypi.org/project/flask/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)