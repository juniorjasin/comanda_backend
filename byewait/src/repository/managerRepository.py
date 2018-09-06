from repository import repo
from utils.logger import Logger
from exceptions import exceptions
import bcrypt

logger = Logger('managerRepo')


class ManagerRepo(repo.Repo):
    def __init__(self):
        super(ManagerRepo, self).__init__()
        logger.debug("managerRepo")
    
    def validarUsuario(self, username_ingresado, password_ingresada):        
        logger.debug('validarManager managerRepo')        
        respuesta = {}
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_manager, username, password, id_restaurante FROM managers WHERE managers.username = %s"
            cursor.execute(consulta,(username_ingresado,))
            row = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)


        if row == None or len(row) == 0:
            raise exceptions.Unauthorized(3001)

        id_manager, username, password, id_restaurante = row
        logger.debug('resultado de consulta:{}'.format((id_manager, username, password, id_restaurante)))

        # No existe user OR No coincide password
        if row is None or not bcrypt.checkpw(password_ingresada.encode('latin-1'), password.encode('latin-1')):
            logger.error("No existe ningun usuario que coincida con esa informacion")
            raise exceptions.Unauthorized(3001)

        respuesta = { "id": id_manager, "username": username, "id_restaurante":id_restaurante }
        return respuesta

        