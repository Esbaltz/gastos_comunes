from flask import Blueprint, request, jsonify

from controllers.DepartamentoController import DepartamentoController


departamento_blueprint = Blueprint('departamento_blueprint', __name__)

class ResidentView:

    @staticmethod
    @departamento_blueprint.route('/departamento/create', methods=['POST'])
    def create_departamento():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            id_dep = data.get('id_dep')
            numero = data.get('numero')
            piso = data.get('piso')
            tipo = data.get('tipo')
            
            new_departamento = DepartamentoController().create_departamento_controller(id_dep, numero=numero, piso=piso, tipo=tipo)
            return jsonify({"mensaje": "Departamento creado", 
                            "departamento": {"id_Dep": new_departamento.id_dep, "numero": new_departamento.numero, "piso": new_departamento.piso, "tipo":new_departamento.tipo}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para departamento"}), 400
    
    @staticmethod
    @departamento_blueprint.route('/departamentos', methods=['GET'])
    def get_all_resident():
        # Llama al controlador para obtener todos los usuarios
        departamento = DepartamentoController.get_departamento_controller()
        departamento_list = [{"id_dep": departamento.id_dep, "numero": departamento.numero, "piso": departamento.piso, "tipo": departamento.piso} for departamento in departamento]
        return jsonify({"departamentos": departamento_list}), 200