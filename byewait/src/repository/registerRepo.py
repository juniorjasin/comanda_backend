from repository import repo
from utils.logger import Logger
from exceptions import exceptions

logger = Logger('registerRepo')


class RegisterRepo(repo.Repo):
    def __init__(self):
        super(RegisterRepo, self).__init__()
        logger.debug("RegisterRepo")
    
    def registrarUsuario(self,userName,password,email):
        idUsuario = -1        
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT * FROM usuarios WHERE username = %s"
            cursor.execute(consulta,(userName,))
            row = cursor.fetchone()            
            if row != None:
                logger.error("ya existe ese nombre de usuario")
                self.cnx.rollback()
                cursor.close()
                raise exceptions.ConflictException(5001)
            else:
                try:                    
                    consulta = "INSERT INTO usuarios(username, email, password) VALUES(%s,%s,%s)"
                    cursor.execute(consulta,(userName, email,password))
                    idUsuario = cursor.lastrowid
                    self.cnx.commit()
                    cursor.close()
                except Exception as ex:
                    self.cnx.rollback()
                    cursor.close()
                    messg = "Fallo la consulta a la base de datos: {}".format(ex)
                    logger.error(messg)                    
                    raise exceptions.InternalServerError(5001)
        except exceptions.ConflictException as ex:
            raise(ex)
        except exceptions.InternalServerError as ex:
            raise(ex)
        except Exception as e:
            messg = "Fallo la consulta a la base de datos: {}".format(e)
            logger.error(messg)
            raise exceptions.InternalServerError(5001)

        respuesta = {
            "id":idUsuario,
            "username":userName,
            "email":email,            
        }
        return respuesta
        