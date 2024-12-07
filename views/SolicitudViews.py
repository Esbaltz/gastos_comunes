from flask import Blueprint, request, jsonify

from controllers.SolicitudController import SolicitudController

solicitud_blueprint = Blueprint('solicitud_blueprint', __name__)

class SolicitudView:
    @staticmethod
    @solicitud_blueprint.route('/solicitud/create', methods=['POST'])
    def create_solicitud():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            id_s = data.get('id_s')
            tipo = data.get('tipo')
            fecha = data.get('fecha')
            estado = data.get('estado')
            descripcion = data.get('descripcion')
            
            new_solicitud = SolicitudController().create_solcitud_controller(id_s, tipo=tipo, fecha=fecha, estado=estado, descripcion=descripcion)
            return jsonify({"mensaje": "Solicitud creada", 
                            "Solicitud": {"id_s": new_solicitud.id_s, "tipo": new_solicitud.tipo, "fecha": new_solicitud.fecha, "estado": new_solicitud.estado, "descripcion": new_solicitud.descripcion}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para solicitud"}), 400
    
    @staticmethod
    @solicitud_blueprint.route('/solicitudes', methods=['GET'])
    def get_all_solicitudes():
        # Llama al controlador para obtener todos los usuarios
        solicitud = SolicitudController.get_solcitud_controller()
        solicitud_list = [{"id_s": solicitud.id_s, "tipo": solicitud.tipo, "fecha": solicitud.fecha, "estado": solicitud.estado, "descripcion": solicitud.descripcion} for solicitud in solicitud]
        return jsonify({"solicitudes": solicitud_list}), 200