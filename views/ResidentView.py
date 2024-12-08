from flask import Blueprint, request, jsonify

from controllers.ResidentController import ResidentController
from models.ResidentModel import TipoResidencia


resident_blueprint = Blueprint('resident_blueprint', __name__)

class ResidentView:
    
    @staticmethod
    @resident_blueprint.route('/residents/create', methods=['POST'])
    def create_resident():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            nombre = data.get('nombre')
            rut = data.get('rut')
            tipo_residencia = TipoResidencia[data['tipo_residencia']]
            departamentos = data.get('departamentos')
            
            new_resident = ResidentController().create_resident_controller(rut, nombre=nombre, tipo_residencia=tipo_residencia, departamentos=departamentos)
            return jsonify({"mensaje": "Residente creado", 
                            "residente": {"rut": new_resident.rut, "nombre": new_resident.nombre, "tipo_residencia": new_resident.tipo_residencia, "departamentos": [dep.id_dep for dep in new_resident.departamentos]}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para tipo_residencia"}), 400
    
    @staticmethod
    @resident_blueprint.route('/residents', methods=['GET'])
    def get_all_resident():
        # Llama al controlador para obtener todos los usuarios
        resident = ResidentController.get_resident_controller()
        resident_list = [{"rut": resident.rut, "nombre": resident.nombre, "tipo_residencia": resident.tipo_residencia.name, "departamentos": [dep.id_dep for dep in resident.departamentos]} for resident in resident]
        return jsonify({"residentes": resident_list}), 200