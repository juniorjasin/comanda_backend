from repository import repo
from utils.logger import Logger
from exceptions import  exceptions
import pymysql
from collections import namedtuple
from model.restaurante import Restaurante

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
            query = "SELECT id_restaurante, name, description, address, image_url from restaurants"            
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
                        # por cada restaurante, deberia obtener todos tags
                        # asi despues los meto en la estrucutra Restaurante
                        tags = self.getAllRestaurantsTags(row[0])
                        r = Restaurante(id=row[0], name=row[1], description=row[2], address=row[3], image_url=row[4], tags=tags)
                        restaurantes.append(r)
                except Exception as e:
                    msg = "Fallo la creacion del array de restaurantes: {}".format(e)
                    logger.error(msg)
                    raise exceptions.InternalServerError(5001)
        except Exception as e2:
            msg = "Fallo la consulta de getAllRestaurants a la base de datos: {}".format(e2)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return restaurantes

    def getAllRestaurantsTags(self, id_restaurante):
        tags = []

        cursor = self.cnx.cursor()
        query = "SELECT tags.nombre \
                   FROM tags_restaurants \
                   JOIN tags \
                     ON tags_restaurants.id_tag = tags.id_tag \
                  WHERE tags_restaurants.id_restaurante = %s"
        values = (id_restaurante)
        cursor.execute(query, values)
        rows = cursor.fetchall()

        for row in rows:
            tags.append(row[0])

        self.cnx.commit()
        cursor.close()

        return tags
        
        