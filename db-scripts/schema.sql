-- creacion de tablas a ejecutar MYSQL
drop table item_menu;
drop table categorias;
drop table restaurants; 

create table if not exists restaurants (
    id_restaurante      integer         not null AUTO_INCREMENT,
    name                varchar(100)    not null,
    description         varchar(500)    not null,
    address           varchar(500)    not null,
    image_url           varchar(500)    not null,
    PRIMARY KEY (id_restaurante)
);


-- test para tablas
INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Antares', 'Cerveceria', 'San Lorenzo 79, Nueva Cordoba', 'https://comercioyjusticia.info/wp-content/uploads/2016/11/Antares.jpg');

INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Fresco', 'Restaurante', 'Jose Manuel Estrada 18, Nueva Cordoba', 'http://s3-us-west-2.amazonaws.com/puntoapunto.com.ar/wp-content/uploads/2017/02/21161917/Fresco.jpg');

INSERT INTO restaurants (name, description, address, image_url)
VALUES ('Peñon', 'Cerveceria', ' Belgrano 902, Güemes', 'http://wpc.72c72.betacdn.net/8072C72/vos-images/sites/default/files/styles/landscape_1020_560/public/nota_periodistica/14_Jul_2016_18_04_01_penon.jpg');



create table if not exists categorias (
    id_categoria         integer         not null AUTO_INCREMENT,
    nombre_categoria     varchar(100)    not null,
    imagen_categoria varchar(255)    not null
    PRIMARY KEY (id_categoria)
);

INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Hamburguesas", "https://image.flaticon.com/icons/svg/174/174387.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Pizzas", "https://image.flaticon.com/icons/svg/174/174359.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Cervezas", "https://image.flaticon.com/icons/svg/174/174403.svg");


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


INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Hamburguesa Completa","Hamburguesa con tomate, lechuga, etc", "120", "https://static.vix.com/es/sites/default/files/styles/large/public/imj/elgranchef/%20Como-hacer-una-clasica-hamburguesa-americana-3.jpg?itok=8__wz6hs");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Hamburguesa Bacon","Hamburguesa con bacon, queso, etc", "145", "http://zasca.ninja/wp-content/uploads/2015/10/hamburguesa.png");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 1, "Fugazza con queso","Pizza de base sencilla con cebolla, un poco de parmesano y con mozzarella", "140", "https://www.thespruceeats.com/thmb/9B7SdcCQkHNPnwoIcKUuDb0o9Xs=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/fugazetta1-57bb81193df78c876338f907.jpg");

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Cerveza IPA", "Es un estilo de cerveza de tradición inglesa que se caracteriza como una ale pálida y espumosa con un alto nivel del alcohol y de lúpulo", "110", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Fuller%27s_India_pale_ale.jpg/220px-Fuller%27s_India_pale_ale.jpg");


drop table items_pedido; 
drop table pedidos; 
drop table usuarios; 

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

