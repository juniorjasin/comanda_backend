from repository import repo
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('loginRepo')


class LoginRepo(repo.Repo):
    def __init__(self):
        super(LoginRepo, self).__init__()
        logger.debug("loginRepo")
    
    def validarUsuario(self,username,password):        
        logger.debug('validarUsuario loginRepo')        
        respuesta = {}
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT id_usuario, username, password FROM usuarios WHERE usuarios.username = %s AND usuarios.password = %s"
            cursor.execute(consulta,(username,password,))
            row = cursor.fetchone()
            self.cnx.commit()
            cursor.close()
            if row != None:                  
                respuesta = {
                                "id": row[0],
                                "username": row[1],
                                "password":row[2]
                            }
                            
            else:                
                raise exceptions.NotFound(3001)
        except exceptions.NotFound as ex:
            logger.error("no existe ningun usuario que coincida con esa informacion")
            raise(ex)
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(e)
            raise exceptions.InternalServerError(5001)        
        return respuesta

        