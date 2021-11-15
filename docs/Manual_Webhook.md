# Webhook
  
With this module you can work with webhook in Rocketbot, how to wait for a request before continuing with the flow of 
your robot  
  
![banner](/docs/imgs/Banner_Webhook.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  



## Descripción de los comandos

### Crear webhook
  
Con este comando puedes crear un webhook para que el robot escuche una petición antes de continuar, la url será 
'0.0.0.0:port/endpoint'
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Endpoint|Endpoint where you need create a request, by default will be '/'|/webhook|
|Puerto|Port where you need create a webwook, by default will be '5005'|5005|
  
![create_endpoint](imgs/create_endpoint.png)