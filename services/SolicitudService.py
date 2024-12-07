from models.SolicitudModel import db, Solicitud

class SolicitudService:
    @staticmethod
    def create_solcitud(id_s, tipo, fecha, estado, descripcion):
        # Crea el objeto
        solicitud = Solicitud(id_s=id_s, tipo=tipo, fecha=fecha, estado=estado, descripcion=descripcion)
        # Agrega el objeto a la bd relacional (usando ORM)
        db.session.add(solicitud)
        db.session.commit()
        return solicitud
    
    @staticmethod
    def get_all_solicitudes():
        return Solicitud.query.all()    