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


To get data from Rocketbot, you must query the url 'localhost:port/:enpoint/:uuid'.
This will return a JSON response in the following format:

    {
        "status": True",
        "data": datos_desde_rocketbot
    }

---

## Como usar este módulo
Para usar este módulo, necesitas tener disponible el puerto que quieras usar como webhook.

### Exponer el webhook con NGROK (Opcional)
1. Descargar NGROK (https://ngrok.com/download)
2. Descomprimir el archivo
3. Ejecute ngrok y ejecute el comando "ngrok http port-number" Aquí el port-number es: 5002
Una vez que ejecute el comando anterior se expondrán dos URLs. Una para HTTP y otra para HTTPS. Puedes utilizar cualquiera de ellas.
4. Copie la URL pública del HTTP y del HTTP.
![NGROK](imgs/ngrok.png)

### Como usar el webhook

Al ejecutar el comando de 'Crear webhook', rocketbot se pausará esperando que se consulte la url configurada en el comando, ya sea con una petición GET o POST. Si la petición es GET, los datos a enviar deben estar en la URL. Si la petición es POST, los datos deben estar en el cuerpo de la petición.

Esto retornará una respuesta en JSON con el siguiente formato:

    {
        "status": True,
        "uuid": "2c9f8f7e-b8e7-4b5b-b8e7-4b5b8e7b8e7b"
    }

Para obtener datos desde Rocketbot, debes consultar la url 'localhost:port/:enpoint/:uuid'.
Esto retornará una respuesta en JSON con el siguiente formato:

    {
        "status": "ok",
        "data": datos_desde_rocketbot
    }

---




