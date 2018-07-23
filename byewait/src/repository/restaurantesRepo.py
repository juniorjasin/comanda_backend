from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from model.restaurante import Restaurante
from collections import namedtuple

Resto = namedtuple('Resto', 'id name description address url_image')


logger = Logger('restaurantesRepo')

class RestaurantesRepo(repo.Repo):
    def __init__(self):
        super(RestaurantesRepo, self).__init__()
        logger.debug('restaurantesRepo')

    def getAllRestaurants(self):
        logger.debug('getAllRestaurants')
        restaurantes = []

        try:        
            cursor = self.cnx.cursor()
            query = "SELECT id, name, description, direction, image_url FROM restaurants"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()
            if rows == None or len(rows) == 0:     
                logger.debug('No hay ningun restaurante insertado...')       
                return restaurantes
            else:
                try:
                    for row in rows:
                        
                        r = Resto(id=row[0], name=row[1], description=row[2], address=row[3], url_image=row[4])

                        restaurante = {
                        "id":row[0],
                        "name":row[1],
                        "description": row[2],
                        "address": row[3],
                        "image_url":row[4]
                        }
                        restaurantes.append(restaurante)
                except Exception as e:
                    msg = "Fallo la creacion del array de restaurantes: {}".format(e)
                    logger.error(msg)
                    raise exceptions.InternalServerError(5001)
        except Exception as e2:
            msg = "Fallo la consulta de getAllRestaurants a la base de datos: {}".format(e2)
            logger.error(msg)
            raise exceptions.InternalServerError(5002)
        return restaurantes

        
        