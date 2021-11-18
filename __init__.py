# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""


from urllib import request


base_path = tmp_global_obj["basepath"] #get rocketbot directory
cur_path = os.path.join(base_path, 'modules', 'Webhook', 'libs')

if cur_path not in sys.path:
    sys.path.append(cur_path)

class WebhookModule:

    def __init__(self):
        from flask import Flask
        self.app = Flask("webhook_module")

    @staticmethod
    def shutdown_server():
        from flask import request
        func = request.environ.get('werkzeug.server.shutdown')
        print("data", func)
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        

webhook_module = WebhookModule()

try:
    module = GetParams("module")
    
    if module == "create_endpoint":
        endpoint = GetParams("endpoint")
        port = GetParams("puerto")
        method = GetParams("method")

        if not endpoint:
            endpoint = "/"
        if not port:
            port = 5005
        if not method:
            method = "['GET']"
        if not method.startswith("["):
            method = "['" + method + "']"
        method = eval(method)

        @webhook_module.app.route(endpoint, methods=method)
        def stopit():
            global webhook_module
            from flask import request as frequest
            from uuid import uuid4
            try:
                data = {}
                
                if frequest.method == "POST":
                    data = frequest.form
                if frequest.method == "GET":
                    data = frequest.args
                result = GetParams("result")
                uuid = str(uuid4())
                if result:
                    SetVar(result, {**dict(data), "uuid": uuid})
                webhook_module.shutdown_server()
                return {"status": True, "uuid": uuid}
            except Exception as e:
                PrintException()
                
                pass
            return {"status": False}

        
        @webhook_module.app.route(endpoint + "/<uuid>", methods=["GET"])
        def getData(uuid):
            global webhook_module
            from flask import request as frequest
            from uuid import uuid4
            try:
                response = GetParams("response")
                if response:
                    response = eval(response)

                return {"status": True,"data": response[uuid]}
            except Exception as e:
                PrintException()
                pass
            return {"status": False}
            
        webhook_module.app.run(host="0.0.0.0", port=port, debug=False)
        
except Exception as e:
    PrintException()
    raise e