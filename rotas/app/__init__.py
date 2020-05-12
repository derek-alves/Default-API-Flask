from flask import request, jsonify
from flask_api import FlaskAPI 


def create_app(config_name):
    app = FlaskAPI(__name__)
    
    # Cria rota com o metodo e caminho desejado e a função que vai ser esse executado por meio de caminha
    # ex: def exemplo(parametros) 
    @app.route("/", methods = ["GET"])
    def exemplo(num1,num2):
        num1 = num1+num2
        
        return num1
    return app