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
            query = "SELECT id_restaurante, name, description, address, image_url, precio_cubiertos \
                       FROM restaurants"
            cursor.execute(query)
            rows = cursor.fetchall()
            self.cnx.commit()
            cursor.close()

            if rows == None:     
                logger.debug('No hay ningun restaurante insertado...')       
                return restaurantes
            else:
                try:
                    for row in rows:
                        tags = self.getAllRestaurantsTags(row[0])
                        id, name, description, address, image_url, precio_cubiertos = row

                        r = { "id": id, "name": name, "description": description, "address": address,
                              "image_url":image_url, "precio_cubiertos":float(precio_cubiertos), "tags":tags}
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

    def getRestaurantById(self, id_restaurante):
        logger.debug('getRestaurantById')
        restaurante = None
        try:        
            cursor = self.cnx.cursor()
            query = "SELECT id_restaurante, name, description, address, image_url, precio_cubiertos \
                       FROM restaurants \
                      WHERE id_restaurante = %s" 
            cursor.execute(query, (id_restaurante,))
            row = cursor.fetchone()
            self.cnx.commit()
            cursor.close()

            if row is not None:     
                id, name, description, address, image_url, precio_cubiertos = row
                tags = self.getAllRestaurantsTags(id_restaurante)
                restaurante = Restaurante(
                    id=id, 
                    name=name,
                    description=description,
                    address=address, 
                    image_url=image_url, 
                    precio_cubiertos=float(precio_cubiertos),
                    tags=tags)
                

        except Exception as e2:
            msg = "Fallo la consulta de getRestaurantById a la base de datos: {}".format(e2)
            logger.error(msg)
            raise exceptions.InternalServerError(5001)
        return restaurante
    

    def getAllRestaurantsTags(self, id_restaurante):
        tags = []

        cursor = self.cnx.cursor()
        query = "SELECT tags.id_tag, tags.nombre \
                   FROM tags_restaurants \
                   JOIN tags \
                     ON tags_restaurants.id_tag = tags.id_tag \
                  WHERE tags_restaurants.id_restaurante = %s "
        values = (id_restaurante)
        cursor.execute(query, values)
        rows = cursor.fetchall()
        self.cnx.commit()
        cursor.close()

        for row in rows:
            tag = {"id":row[0], "nombre":row[1]}
            tags.append(tag)

        return tags
        
        