-- creacion de tablas a ejecutar MYSQL

create table if not exists dishes (
    id                  integer         not null AUTO_INCREMENT,
    name                varchar(100)    not null,
    description         varchar(500)    not null,
    price               decimal(10,2)   not null,
    restaurant          varchar(200)    not null,
    PRIMARY KEY (id)
);