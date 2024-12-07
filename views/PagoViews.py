from flask import Blueprint, request, jsonify

from controllers.PagoController import PagoController

pago_blueprint = Blueprint('pago_blueprint', __name__)

class PagoView:
    @staticmethod
    @pago_blueprint.route('/pago/create', methods=['POST'])
    def create_pago():
        try:
            # Obtener los datos del cuerpo de la solicitud y crear una resident
            data = request.get_json()
            id_p = data.get('id_p')
            monto = data.get('monto')
            fecha = data.get('fecha')
            estado = data.get('estado')
            
            new_pago = PagoController().create_pago_controller(id_p, monto=monto, fecha=fecha, estado=estado)
            return jsonify({"mensaje": "Pago creado", 
                            "Pago": {"id_p": new_pago.id_p, "monto": new_pago.monto, "fecha": new_pago.fecha, "estado":estado}}), 201
        
        except KeyError as e:
            return jsonify({"error": f"Falta el campo {str(e)}"}), 400
        except ValueError as e:
            return jsonify({"error": "Valor inválido para pago"}), 400
    
    @staticmethod
    @pago_blueprint.route('/pagos', methods=['GET'])
    def get_all_pagos():
        # Llama al controlador para obtener todos los usuarios
        pago = PagoController.get_pago_controller()
        pago_list = [{"id_p": pago.id_p, "monto": pago.monto, "fecha": pago.fecha, "estado": pago.estado} for pago in pago]
        return jsonify({"pagos": pago_list}), 200