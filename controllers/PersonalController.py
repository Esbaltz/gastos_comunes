from services.PersonalService import PersonalService

class PersonalController:
    @staticmethod
    def create_personal_controller(rut, nombre, cargo, horario):
        return PersonalService.create_resident(rut, nombre, cargo, horario)
    
    @staticmethod
    def get_personal_controller():
        return PersonalService.get_all_personal()