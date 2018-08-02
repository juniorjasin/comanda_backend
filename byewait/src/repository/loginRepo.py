from repository import repo
from utils.logger import Logger
from exceptions import exceptions
import bcrypt

logger = Logger('loginRepo')


class LoginRepo(repo.Repo):
    def __init__(self):
        super(LoginRepo, self).__init__()
        logger.debug("loginRepo")
    
    def validarUsuario(self, username, password):        
        logger.debug('validarUsuario loginRepo')        
        respuesta = {}
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_usuario, username, password FROM usuarios WHERE usuarios.username = %s"
            cursor.execute(consulta,(username,))
            row = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            if row is None: # No existe user
                raise exceptions.NotFound(3001)
            if not bcrypt.checkpw(password.encode('latin-1'), row[2].encode('latin-1')): # No coincide password
                raise exceptions.Unauthorized(3001)
            respuesta = { "id": row[0], "username": row[1], "password": row[2]}
        except exceptions.NotFound as notFoundException:
            logger.error("No existe ningun usuario que coincida con esa informacion")
            raise(notFoundException)
        except exceptions.Unauthorized as unauthorizedException:
            logger.error("Usuario no autorizado")
            raise(unauthorizedException)
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)
        return respuesta

        