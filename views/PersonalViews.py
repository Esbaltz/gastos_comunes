from flask import Blueprint, request, jsonify

from controllers.PersonalController import PersonalController

personal_blueprint = Blueprint('personal_blueprint', __name__)

class PersonalView:
    @staticmethod
    @personal_blueprint.route('/personal/create', methods=['POST'])
    def create_personal():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            id_p = data.get('id_p')
            nombre = data.get('nombre')
            cargo = data.get('cargo')
            horario = data.get('horario')
            
            new_personal = PersonalController().create_personal_controller(id_p, nombre=nombre, cargo=cargo, horario=horario)
            return jsonify({"mensaje": "Personal creado", 
                            "Personal": {"id_p": new_personal.id_p, "nombre": new_personal.nombre, "cargo": new_personal.cargo, "horario":new_personal.horario}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para personal"}), 400
    
    @staticmethod
    @personal_blueprint.route('/personal', methods=['GET'])
    def get_all_personal():
        # Llama al controlador para obtener todos los usuarios
        personal = PersonalController.get_personal_controller()
        personal_list = [{"id_p": personal.id_p, "nombre": personal.nombre, "cargo": personal.cargo, "horario": personal.horario} for personal in personal]
        return jsonify({"personal": personal_list}), 200