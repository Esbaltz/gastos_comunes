from services.EdificioService import EdificioService

class EdificioController:
    @staticmethod
    def create_edificio_controller(id_e, nombre, ubicacion, cantPisos, cantDeptos):
        return EdificioService.create_resident(id_e, nombre, ubicacion, cantPisos, cantDeptos)
    
    @staticmethod
    def get_edificio_controller():
        return EdificioService.get_all_edificios()