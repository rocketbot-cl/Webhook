
# Webhook
  
Con este módulo podrás trabajar con webhook en Rocketbot, como esperar una petición antes de continuar con el flujo de 
tu robot  
  
![banner](/docs/imgs/Banner_Webhook.png)
## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de rocketbot.  




## Como usar este módulo
Para usar este módulo, necesitas tener disponible el puerto que quieras usar como webhook.


### Exponer el webhook con NGROK
1. Descargar NGROK (https://ngrok.com/download)
2. Descomprimir el archivo
3. Ejecute 
ngrok y ejecute el comando "ngrok http port-number" Aquí el port-number es: 5002
Una vez que ejecute el comando anterior
 se expondrán dos URLs. Una para HTTP y otra para HTTPS. Puedes utilizar cualquiera de ellas.
4. Copie la URL pública 
del HTTP y del HTTP.
![NGROK](imgs/ngrok.png)


## Descripción de los comandos

### Crear webhook
  
Con este comando puedes crear un webhook para que el robot escuche una petición antes de continuar, la url será 
'0.0.0.0:port/endpoint'
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Endpoint|Endpoint where you need create a request, by default will be '/'|/webhook|
|Puerto|Port where you need create a webwook, by default will be '5005'|5005|
