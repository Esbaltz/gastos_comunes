from services.PagoService import PagoService

class PagoController:
    @staticmethod
    def create_pago_controller(id_p, monto, fecha, estado):
        return PagoService.create_pago(id_p, monto, fecha, estado)
    
    @staticmethod
    def get_pago_controller():
        return PagoService.get_all_pagos()