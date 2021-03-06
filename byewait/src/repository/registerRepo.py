from repository import repo
from utils.logger import Logger
from exceptions import exceptions
import bcrypt

logger = Logger('registerRepo')

class RegisterRepo(repo.Repo):
    def __init__(self):
        super(RegisterRepo, self).__init__()
        logger.debug("RegisterRepo")
    
    def registrarUsuario(self, userName, password, nombre, apellido, email):
        idUsuario = -1
        try:
            cursor = self.cnx.cursor()
            consulta = "SELECT * \
                          FROM usuarios \
                         WHERE username = %s"
            cursor.execute(consulta,(userName,))
            row = cursor.fetchone()     

            if row != None:
                logger.error("Ya existe ese nombre de usuario")
                cursor.close()
                raise exceptions.ConflictException(5001)

            else:
                try:
                    hashedPassword = bcrypt.hashpw(password.encode('latin-1'), bcrypt.gensalt())
                    consulta = "INSERT INTO usuarios(username, email, password, nombre, apellido) \
                                     VALUES (%s,%s,%s,%s,%s)"
                    cursor.execute(consulta,(userName, email, hashedPassword, nombre, apellido))
                    idUsuario = cursor.lastrowid
                    self.cnx.commit()
                except Exception as ex:
                    self.cnx.rollback()                  
                    raise exceptions.InternalServerError(5001)
                finally:
                    cursor.close()


        except exceptions.ConflictException as ex:
            raise(ex)
        except exceptions.InternalServerError as ex:
            raise(ex)
        except Exception as e:
            logger.error("Fallo la consulta a la base de datos: {}".format(e))
            raise exceptions.InternalServerError(5001)

        respuesta = {
            'id': idUsuario,
            'username': userName,
            'email': email,
            'nombre': nombre,
            'apellido': apellido
        }

        return respuesta
        