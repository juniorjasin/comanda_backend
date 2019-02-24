import unittest
import pymysql

class Test(unittest.TestCase):
    def setUp(self):
        
        cnx = pymysql.connect(db="byewait", user="dev", passwd="changeme", port=3307, host="localhost")
        cursor = cnx.cursor()

        # cursor.execute('delete from managers')
        # cursor.execute('delete from tags_restaurants')
        cursor.execute('delete from scores_item_menu')
        # cursor.execute('delete from tags')
        # cursor.execute('delete from opciones_items_pedido')
        cursor.execute('delete from items_pedido')
        cursor.execute('delete from pedidos')
        cursor.execute('delete from usuarios')
        # cursor.execute('delete from item_menu_opciones_item_menu')
        # cursor.execute('delete from detalle_opciones_item_menu')
        # cursor.execute('delete from opciones_item_menu')
        # cursor.execute('delete from item_menu')
        # cursor.execute('delete from subcategorias_categorias')
        # cursor.execute('delete from categorias')
        # cursor.execute('delete from restaurants')

        # # Resetear los auto_increment para que los tests puedan acceder correctamente a los ids
        # cursor.execute('ALTER TABLE managers AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE tags_restaurants AUTO_INCREMENT = 1')
        cursor.execute('ALTER TABLE scores_item_menu AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE tags AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE opciones_items_pedido AUTO_INCREMENT = 1')
        cursor.execute('ALTER TABLE items_pedido AUTO_INCREMENT = 1')
        cursor.execute('ALTER TABLE pedidos AUTO_INCREMENT = 1')
        cursor.execute('ALTER TABLE usuarios AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE item_menu_opciones_item_menu AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE detalle_opciones_item_menu AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE opciones_item_menu AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE item_menu AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE subcategorias_categorias AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE categorias AUTO_INCREMENT = 1')
        # cursor.execute('ALTER TABLE restaurants AUTO_INCREMENT = 1')




        cnx.commit()
        cursor.close()
        cnx.close()

    def tearDown(self):
        pass
