from flask import Blueprint, request, jsonify

from controllers.EdificioController import EdificioController

edificio_blueprint = Blueprint('edificio_blueprint', __name__)

class EdificioView:
    @staticmethod
    @edificio_blueprint.route('/edificio/create', methods=['POST'])
    def create_edificio():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            id_e = data.get('id_e')
            nombre = data.get('nombre')
            ubicacion = data.get('ubicacion')
            cantPisos = data.get('cantPisos')
            cantDeptos = data.get('cantDeptos')
            
            new_edificio = EdificioController().create_edificio_controller(id_e, nombre=nombre, ubicacion=ubicacion, cantPisos=cantPisos, cantDeptos=cantDeptos)
            return jsonify({"mensaje": "Edificio creado", 
                            "Edificio": {"id_e": new_edificio.id_e, "nombre": new_edificio.nombre, "ubicacion": new_edificio.ubicacion, "cantPisos":new_edificio.cantPisos, "cantDeptos": new_edificio.cantDeptos}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para edificio"}), 400
    
    @staticmethod
    @edificio_blueprint.route('/edificios', methods=['GET'])
    def get_all_edificios():
        # Llama al controlador para obtener todos los usuarios
        edificio = EdificioController.get_edificio_controller()
        edificio_list = [{"id_e": edificio.id_e, "nombre": edificio.nombre, "ubicacion": edificio.ubicacion, "cantPisos": edificio.cantPisos, "cantDeptos": edificio.cantDeptos} for edificio in edificio]
        return jsonify({"edificios": edificio_list}), 200