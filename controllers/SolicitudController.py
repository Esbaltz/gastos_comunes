from services.SolicitudService import SolicitudService

class SolicitudController:
    @staticmethod
    def create_solcitud_controller(id_s, tipo, fecha, estado, descripcion):
        return SolicitudService.create_solicitud(id_s, tipo, fecha, estado, descripcion)
    
    @staticmethod
    def get_solcitud_controller():
        return SolicitudService.get_all_solicitudes()