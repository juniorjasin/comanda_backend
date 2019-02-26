from repository import repo
from utils.logger import Logger
from exceptions import exceptions
import bcrypt
from tornado import gen

logger = Logger('loginRepo')


class LoginRepo(repo.Repo):
    def __init__(self):
        super(LoginRepo, self).__init__()
        logger.debug("loginRepo")
    
    def validarUsuario(self, usernameOrEmail, password):        
        logger.debug('validarUsuario loginRepo')        
        respuesta = {}
        try:
            
            cursor = self.cnx.cursor()
            consulta = "SELECT id_usuario, username, password, nombre, apellido \
                          FROM usuarios \
                         WHERE username = %s \
                            OR email = %s "
            cursor.execute(consulta,(usernameOrEmail, usernameOrEmail))
            row = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            
            try:
                id_usuario, username, store_password, nombre, apellido = row
                if not bcrypt.checkpw(password.encode('latin-1'), store_password.encode('latin-1')):
                   raise exceptions.Unauthorized(3001) 
                
                respuesta = { 'id': id_usuario, 'username': username, 'nombre': nombre, 'apellido': apellido }
                
            except Exception as e:
                raise exceptions.Unauthorized(3001)


        except exceptions.Unauthorized as e:
            logger.error("No existe ningun usuario que coincida con esa informacion")
            raise e
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)

        return respuesta

        