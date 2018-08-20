-- creacion de tablas a ejecutar MYSQL
drop table items_pedido; 
drop table pedidos; 
drop table usuarios; 
drop table item_menu;
drop table categorias;
drop table restaurants; 

create table if not exists restaurants (
    id_restaurante      integer         not null AUTO_INCREMENT,
    name                varchar(100)    not null,
    description         varchar(500)    not null,
    address             varchar(500)    not null,
    image_url           varchar(500)    not null,
    PRIMARY KEY (id_restaurante)
);


-- test para tablas
INSERT INTO restaurants (name, description, address, image_url)
VALUES ('La Mamma', 'Restaurante', 'Av. Rafael Núñez 6092, 5021 Córdoba', 'http://34.230.44.202:8888/images/1-lamamma_logo4.jpg');

INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Fresco', 'Restaurante', 'Jose Manuel Estrada 18, Nueva Cordoba', 'http://34.230.44.202:8888/images/2-fresco_logo1.jpg');

INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Peñon', 'Cerveceria', ' Belgrano 902, Güemes', 'http://34.230.44.202:8888/images/3-penon_logo1.jpg');

INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Antares', 'Cerveceria', 'San Lorenzo 79, Nueva Cordoba', 'http://34.230.44.202:8888/images/1-antares_logo2.jpg');



create table if not exists categorias (
    id_categoria        integer         not null AUTO_INCREMENT,
    nombre_categoria    varchar(100)    not null,
    PRIMARY KEY (id_categoria)
);

INSERT INTO categorias (nombre_categoria) VALUES ("Hamburguesas"); -- 1
INSERT INTO categorias (nombre_categoria) VALUES ("Pizzas"); -- 2
INSERT INTO categorias (nombre_categoria) VALUES ("Cervezas"); -- 3
INSERT INTO categorias (nombre_categoria) VALUES ("Gaseosas"); -- 4
INSERT INTO categorias (nombre_categoria) VALUES ("Panchos"); -- 5
INSERT INTO categorias (nombre_categoria) VALUES ("Vinos"); -- 6
INSERT INTO categorias (nombre_categoria) VALUES ("Carnes"); -- 7
INSERT INTO categorias (nombre_categoria) VALUES ("Postres"); -- 8
INSERT INTO categorias (nombre_categoria) VALUES ("Picadas"); -- 9
INSERT INTO categorias (nombre_categoria) VALUES ("Pastas"); -- 10
INSERT INTO categorias (nombre_categoria) VALUES ("Entradas"); -- 11
INSERT INTO categorias (nombre_categoria) VALUES ("Guarniciones"); -- 12
INSERT INTO categorias (nombre_categoria) VALUES ("Platos principales"); -- 13
INSERT INTO categorias (nombre_categoria) VALUES ("Meriendas/Desayunos"); -- 14
INSERT INTO categorias (nombre_categoria) VALUES ("Combos"); -- 15
INSERT INTO categorias (nombre_categoria) VALUES ("Tragos"); -- 16


create table if not exists item_menu (
    id_item_menu        integer         not null AUTO_INCREMENT,
    id_categoria        integer         not null,
    id_restaurante      integer         not null,
    nombre_item_menu    varchar(100)    not null,
    description         varchar(500)    not null,
    precio              varchar(500)    not null,
    image_url           varchar(500)    not null,
    PRIMARY KEY (id_item_menu),
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_restaurante) REFERENCES restaurants(id_restaurante)
);


-- restaurante 1: la mamma
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Trittico de La Mamma","ravioles de lomo y hongos, sorrentinos de mozzarella y nuez y ñoquis en sus respectivas salsas", "190",
"http://34.230.44.202:8888/images/1-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (7, 1, "Carpaccio de salmone affumicato","salmon acompañado de un riquisimo queso blanco y alcaparras", "210",
"http://34.230.44.202:8888/images/1-2.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (7, 1, "Pacu de verduras grilladas","delicioso pacu horneado con mix de verduras grilladas", "200",
"http://34.230.44.202:8888/images/1-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Controfiletto hongroisse", "Entrecorte en crema de hongos acompañado de brocolis a la parmesana", "215",
"http://34.230.44.202:8888/images/1-4.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Antipasto italiano", "antipasto con cebolla picada, berenjenas, zucchini, pimiento y aceite de oliva", "90",
"http://34.230.44.202:8888/images/1-5.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Sorrentinos con salsa", "sorrentinos con salsa bolognesa y albaca", "190",
"http://34.230.44.202:8888/images/1-6.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Sorrentini nerodi seppia", "sorrentino negro relleno con trucha y salmon ahumado", "290",
"http://34.230.44.202:8888/images/1-7.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Fideos clasicos", "fideos caseros con salsa bolognesa y albaca", "180",
"http://34.230.44.202:8888/images/1-8.jpg");


-- restaurante 2: fresco
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas al champignon", "papas rusticas con champignon condimentada con especias", "90",
"http://34.230.44.202:8888/images/2-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas fresco", "Papas rusticas con pimiento rojo y verde, cebolla y una lluvia de semillas de chia", "100",
"http://34.230.44.202:8888/images/2-12.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Picada clasica", "tabla con queso roquefort, panceta, salamin, aceitunas negras, bondiola y tomates cherry", "150",
"http://34.230.44.202:8888/images/2-8.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 2, "Pizza al champignon", "pizza al molde con champignon, jamon, queso y cebolla", "190",
"http://34.230.44.202:8888/images/2-2.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 2, "Rucula y jamon crudo", "pizza al molde con rucula, jamon crudo, queso parmesano y aceitunas negras", "200",
"http://34.230.44.202:8888/images/2-7.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 2, "Hamburguesa completa", "hamburguesa con lechuga, tomate, queso cheda y bacon", "150",
"http://34.230.44.202:8888/images/2-11.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 2, "Tiramisu", "queso mascarpone, vainilla, cacao en polvo, espolvoreado con cafe", "90",
"http://34.230.44.202:8888/images/2-19.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 2, "Chocotorta", "dulce de leche, casancrem, chocolinas, crema y chocolate", "90",
"http://34.230.44.202:8888/images/2-14.jpg");


-- restaurante 3: peñon
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas peñon", "papas fritas con mayonesa casera, bacon y lluvia de verdeo", "90",
"http://34.230.44.202:8888/images/3-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas a caballo", "Papas fritas con huevos y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas con cheddar", "Papas fritas, abundante queso cheddar y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-27.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Fish mix", "mix de rabas y bastones de pescado, con mayonesa casera y limon", "200",
"http://34.230.44.202:8888/images/3-6.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Nachos peñon", "nachos caseros bañados en queso chedar y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-7.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 2, "Combo argento", "chori completo + IPA argenta", "250",
"http://34.230.44.202:8888/images/3-25.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 2, "Combo peñon", "picada con bastones de pollo, rabas y canape con salsas de mayonesa + 2 IPA", "300",
"http://34.230.44.202:8888/images/3-25.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 2, "Combo amigos", "picada clasica + 4 cervezas artesanales a eleccion", "380",
"http://34.230.44.202:8888/images/3-26.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 2, "Combo beer", "2 cervezas artesanales a eleccion (IPA, Scotch, Lager)", "140",
"http://34.230.44.202:8888/images/3-11.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (16, 2, "Mojitos", "ron, zumo de lima, menta, hielo picado y soda", "120",
"http://34.230.44.202:8888/images/3-11.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 2, "Scotch ale", "con una graduación alcohólica cercana a los 5 grados, se distingue además por sus aromas frutales", "380",
"http://34.230.44.202:8888/images/3-5.jpg");


-- restaurante 4: antares
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 2, "Stout", "la stout es una cerveza de color casi negro, oscura, amarga y elaborada con malta de cebada tostada", "80",
"http://34.230.44.202:8888/images/4-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 2, "Lager", "cerveza de sabor ligero, de aroma y sabor mas sutil, equilibrado y limpio", "80",
"http://34.230.44.202:8888/images/4-2.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 2, "Ale", "cerveza de sabor ligero, de aroma y sabor mas sutil, equilibrado y limpio", "80",
"http://34.230.44.202:8888/images/4-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Nachos antares", "nachos bañados con queso chedar y palta y lluvia de aceitunas negras", "120",
"http://34.230.44.202:8888/images/4-4.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Papas antares", "papas fritas con mayonesa casera, bacon y lluvia de pimientos", "80",
"http://34.230.44.202:8888/images/4-5.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 2, "Rabas", "rabas frescas con mayonesa casera y limon", "150",
"http://34.230.44.202:8888/images/4-6.jpg");



create table if not exists usuarios (
    id_usuario          integer         not null AUTO_INCREMENT,
    username            varchar(100)    not null UNIQUE,
    email               varchar(100)    not null,
    password            varchar(400)    not null,
    PRIMARY KEY (id_usuario)
);

INSERT INTO usuarios (username, email, password) VALUES ('juan', 'juan@gmail.com', '$2b$12$qxYL/c5KbxDb0iIvVgvrYuow20y7BRgk8JV6BeMQ2Cy1wMrNAabU2');
INSERT INTO usuarios (username, email, password) VALUES ('andi', 'andi@gmail.com', '$2b$12$AftbQ7QacpeB/VOVlXeJT.HEt0NwfNbIKF0NozVxvhZuhKnheeN6m');
INSERT INTO usuarios (username, email, password) VALUES ('jrjs', 'jrjs@gmail.com', '$2b$12$xzcHoLXLOa.bO7XEkqQ8wupvMUFTsMgNnX8.KbxCSEMJ.zfv95DbO');


create table if not exists pedidos (
    id_pedidos          integer         not null AUTO_INCREMENT,
    id_usuario          integer         not null,
    id_mesa             integer         not null,
    fecha_hora          timestamp       not null,
    PRIMARY KEY (id_pedidos),
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario)
);



create table if not exists items_pedido (
    id_item_menu        integer         not null,
    id_pedidos          integer         not null,
    cantidad            integer         not null,
    aclaraciones        varchar(500)    not null,
    PRIMARY KEY (id_item_menu, id_pedidos),
    FOREIGN KEY(id_item_menu) REFERENCES item_menu(id_item_menu),
    FOREIGN KEY(id_pedidos) REFERENCES pedidos(id_pedidos)
);

