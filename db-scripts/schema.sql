-- creacion de tablas a ejecutar MYSQL
drop table restaurants;

create table if not exists restaurants (
    id                  integer         not null AUTO_INCREMENT,
    name                varchar(100)    not null,
    description         varchar(500)    not null,
    direction           varchar(500)    not null,
    image_url           varchar(500)    not null,
    PRIMARY KEY (id)
);


-- test para tablas
INSERT INTO restaurants (name, description, direction, image_url)
VALUES ('Antares', 'Cerveceria', 'San Lorenzo 79, Nueva Cordoba', 'https://comercioyjusticia.info/wp-content/uploads/2016/11/Antares.jpg');

INSERT INTO restaurants (name, description, direction, image_url)
VALUES ('Fresco', 'Restaurante', 'Jose Manuel Estrada 18, Nueva Cordoba', 'http://s3-us-west-2.amazonaws.com/puntoapunto.com.ar/wp-content/uploads/2017/02/21161917/Fresco.jpg');

INSERT INTO restaurants (name, description, direction, image_url)
VALUES ('Peñon', 'Cerveceria', ' Belgrano 902, Güemes', 'http://wpc.72c72.betacdn.net/8072C72/vos-images/sites/default/files/styles/landscape_1020_560/public/nota_periodistica/14_Jul_2016_18_04_01_penon.jpg');