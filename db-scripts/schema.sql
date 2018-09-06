-- creacion de tablas a ejecutar MYSQL
drop trigger update_item_menu_rating_on_delete;
drop trigger update_item_menu_rating_on_update;
drop trigger update_item_menu_rating_on_insert;

drop table managers;
drop table tags_restaurants;
drop table scores_item_menu;
drop table tags;
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
VALUES ('Antares', 'Cerveceria', 'San Lorenzo 79, Nueva Cordoba', 'http://34.230.44.202:8888/images/4-antares_logo4.jpg');


create table if not exists categorias (
    id_categoria         integer         not null AUTO_INCREMENT,
    nombre_categoria     varchar(100)    not null,
    imagen_categoria varchar(255)    not null,
    PRIMARY KEY (id_categoria)
);

INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Hamburguesas", "https://image.flaticon.com/icons/svg/174/174387.svg"); -- 1
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Pizzas", "https://image.flaticon.com/icons/svg/174/174359.svg"); -- 2
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Cervezas", "https://image.flaticon.com/icons/svg/174/174403.svg"); -- 3
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Gaseosas", "https://image.flaticon.com/icons/svg/81/81940.svg"); -- 4
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Panchos", "https://image.flaticon.com/icons/svg/1064/1064941.svg"); -- 5
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Vinos", "https://image.flaticon.com/icons/svg/120/120992.svg"); -- 6
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Carnes", "https://image.flaticon.com/icons/svg/933/933310.svg"); -- 7
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Postres", "https://image.flaticon.com/icons/svg/768/768230.svg"); -- 8
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Picadas", ""); -- 9
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Pastas", "https://image.flaticon.com/icons/svg/701/701980.svg"); -- 10
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Entradas", "https://image.flaticon.com/icons/svg/560/560348.svg"); -- 11
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Guarniciones", "https://image.flaticon.com/icons/svg/158/158497.svg"); -- 12
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Platos principales", "https://image.flaticon.com/icons/svg/1046/1046874.svg"); -- 13
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Meriendas/Desayunos", "https://image.flaticon.com/icons/svg/633/633652.svg"); -- 14
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Combos", "https://image.flaticon.com/icons/svg/584/584648.svg"); -- 15
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Tragos", "https://image.flaticon.com/icons/svg/1002/1002224.svg"); -- 16


create table if not exists item_menu (
    id_item_menu        integer         not null AUTO_INCREMENT,
    id_categoria        integer         not null,
    id_restaurante      integer         not null,
    nombre_item_menu    varchar(100)    not null,
    description         varchar(500)    not null,
    precio              varchar(500)    not null,
    image_url           varchar(500)    not null,
    rating              decimal(4,2)    null      check (rate >= 0 and rate <= 5),
    PRIMARY KEY (id_item_menu),
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_restaurante) REFERENCES restaurants(id_restaurante)
);


-- restaurante 1: la mamma
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Trittico de La Mamma","ravioles de lomo y hongos, sorrentinos de mozzarella y nuez y ñoquis en sus respectivas salsas", "190",
"http://34.230.44.202:8888/images/1-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Sorrentinos con salsa", "sorrentinos con salsa bolognesa y albaca", "190",
"http://34.230.44.202:8888/images/1-6.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Sorrentini nerodi seppia", "sorrentino negro relleno con trucha y salmon ahumado", "290",
"http://34.230.44.202:8888/images/1-7.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Fideos clasicos", "fideos caseros con salsa bolognesa y albaca", "180",
"http://34.230.44.202:8888/images/1-8.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Carpaccio de salmone affumicato","salmon acompañado de un riquisimo queso blanco y alcaparras", "210",
"http://34.230.44.202:8888/images/1-2.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Pacu de verduras grilladas","delicioso pacu horneado con mix de verduras grilladas", "200",
"http://34.230.44.202:8888/images/1-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Controfiletto hongroisse", "Entrecorte en crema de hongos acompañado de brocolis a la parmesana", "215",
"http://34.230.44.202:8888/images/1-4.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Antipasto italiano", "antipasto con cebolla picada, berenjenas, zucchini, pimiento y aceite de oliva", "90",
"http://34.230.44.202:8888/images/1-5.jpg");



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
VALUES (11, 3, "Papas peñon", "papas fritas con mayonesa casera, bacon y lluvia de verdeo", "90",
"http://34.230.44.202:8888/images/3-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 3, "Papas a caballo", "Papas fritas con huevos y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 3, "Papas con cheddar", "Papas fritas, abundante queso cheddar y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-27.png");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 3, "Fish mix", "mix de rabas y bastones de pescado, con mayonesa casera y limon", "200",
"http://34.230.44.202:8888/images/3-6.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 3, "Nachos peñon", "nachos caseros bañados en queso chedar y cebolla de verdeo", "120",
"http://34.230.44.202:8888/images/3-7.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 3, "Combo argento", "chori completo + IPA argenta", "250",
"http://34.230.44.202:8888/images/3-25.png");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 3, "Combo peñon", "picada con bastones de pollo, rabas y canape con salsas de mayonesa + 2 IPA", "300",
"http://34.230.44.202:8888/images/3-23.png");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 3, "Combo amigos", "picada clasica + 4 cervezas artesanales a eleccion", "380",
"http://34.230.44.202:8888/images/3-26.png");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (15, 3, "Combo beer", "2 cervezas artesanales a eleccion (IPA, Scotch, Lager)", "140",
"http://34.230.44.202:8888/images/3-11.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (16, 3, "Mojitos", "ron, zumo de lima, menta, hielo picado y soda", "120",
"http://34.230.44.202:8888/images/3-12.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 3, "Scotch ale", "con una graduación alcohólica cercana a los 5 grados, se distingue además por sus aromas frutales", "380",
"http://34.230.44.202:8888/images/3-5.jpg");


-- restaurante 4: antares
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 4, "Stout", "la stout es una cerveza de color casi negro, oscura, amarga y elaborada con malta de cebada tostada", "80",
"http://34.230.44.202:8888/images/4-1.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 4, "Lager", "cerveza de sabor ligero, de aroma y sabor mas sutil, equilibrado y limpio", "80",
"http://34.230.44.202:8888/images/4-2.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 4, "Ale", "cerveza de sabor ligero, de aroma y sabor mas sutil, equilibrado y limpio", "80",
"http://34.230.44.202:8888/images/4-3.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 4, "Nachos antares", "nachos bañados con queso chedar y palta y lluvia de aceitunas negras", "120",
"http://34.230.44.202:8888/images/4-4.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 4, "Papas antares", "papas fritas con mayonesa casera, bacon y lluvia de pimientos", "80",
"http://34.230.44.202:8888/images/4-5.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 4, "Rabas", "rabas frescas con mayonesa casera y limon", "150",
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


create table if not exists scores_item_menu (
    id                  integer         not null AUTO_INCREMENT,
    id_item_menu        integer         not null,
    id_usuario          integer         not null,
    score               integer         not null check(score >= 1 and score <= 5),
    PRIMARY KEY (id),
    FOREIGN KEY(id_item_menu)    REFERENCES item_menu(id_item_menu),
    FOREIGN KEY (id_usuario)     REFERENCES usuarios(id_usuario)
);


delimiter |
create trigger update_item_menu_rating_on_insert
  after insert on scores_item_menu
  for each row begin
    update item_menu set rating = (select avg(score) 
                                    from scores_item_menu 
                                   where id_item_menu = new.id_item_menu)
    where id_item_menu = new.id_item_menu;
end
|
delimiter ;

delimiter |
create trigger update_item_menu_rating_on_update
  after update on scores_item_menu
  for each row begin
  update item_menu set rating = (select avg(score) 
                                  from scores_item_menu 
                                 where id_item_menu = new.id_item_menu)
  where id_item_menu = new.id_item_menu;
end
|
delimiter ;

delimiter |
create trigger update_item_menu_rating_on_delete
  after delete on scores_item_menu
  for each row begin
  update item_menu set rating = (select avg(score) 
                                  from scores_item_menu 
                                 where id_item_menu = old.id_item_menu)
  where id_item_menu = old.id_item_menu;
end
|
delimiter ;

INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (1, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (2, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (4, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (5, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (6, 3, 5);

INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (7, 3, 1);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (8, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (9, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (10, 3, 5);
INSERT INTO scores_item_menu (id_item_menu, id_usuario, score) VALUES (11, 3, 5);

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


create table if not exists tags (
    id_tag              integer         not null AUTO_INCREMENT,
    nombre              varchar(100)    not null UNIQUE,
    PRIMARY KEY (id_tag)
);

INSERT INTO tags (nombre) VALUES ('bar');
INSERT INTO tags (nombre) VALUES ('cerveceria');
INSERT INTO tags (nombre) VALUES ('tragos');

INSERT INTO tags (nombre) VALUES ('restaurante');
INSERT INTO tags (nombre) VALUES ('pastas');
INSERT INTO tags (nombre) VALUES ('vinos');



create table if not exists tags_restaurants (
    id_tag              integer         not null,
    id_restaurante      integer         not null,
    PRIMARY KEY (id_tag, id_restaurante),
    FOREIGN KEY(id_tag) REFERENCES tags(id_tag),
    FOREIGN KEY(id_restaurante) REFERENCES restaurants(id_restaurante)
);

-- la mamma
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (4,1);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (5,1);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (6,1);

-- fresco, peñon, antares
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (1,2);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (2,2);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (3,2);

INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (1,3);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (2,3);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (3,3);

INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (1,4);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (2,4);
INSERT INTO tags_restaurants (id_tag, id_restaurante) VALUES (3,4);


create table if not exists managers (
    id_manager          integer         not null AUTO_INCREMENT,
    username            varchar(100)    not null UNIQUE,
    email               varchar(100)    not null,
    id_restaurante      integer         not null,
    password            varchar(400)    not null,
    FOREIGN KEY(id_restaurante) REFERENCES restaurants(id_restaurante),
    PRIMARY KEY (id_manager)
);

INSERT INTO managers (username, email, password, id_restaurante) 
VALUES ('jrjs', 'jrjs@gmail.com', '$2b$12$xzcHoLXLOa.bO7XEkqQ8wupvMUFTsMgNnX8.KbxCSEMJ.zfv95DbO', 1);

INSERT INTO managers (username, email, password, id_restaurante) 
VALUES ('juan', 'juan@gmail.com', '$2b$12$qxYL/c5KbxDb0iIvVgvrYuow20y7BRgk8JV6BeMQ2Cy1wMrNAabU2', 2);

INSERT INTO managers (username, email, password, id_restaurante) 
 VALUES ('andi', 'andi@gmail.com', '$2b$12$AftbQ7QacpeB/VOVlXeJT.HEt0NwfNbIKF0NozVxvhZuhKnheeN6m', 3);