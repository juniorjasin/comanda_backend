-- creación de tablas a ejecutar MYSQL
drop trigger update_item_menu_rating_on_delete;
drop trigger update_item_menu_rating_on_update;
drop trigger update_item_menu_rating_on_insert;

drop table managers;
drop table tags_restaurants;
drop table scores_item_menu;
drop table tags;
drop table opciones_items_pedido;
drop table items_pedido;
drop table pedidos;
drop table usuarios;
drop table item_menu_opciones_item_menu;
drop table detalle_opciones_item_menu;
drop table opciones_item_menu;
drop table item_menu;
drop table subcategorias_categorias;
drop table categorias;
drop table restaurants;


create table if not exists restaurants (
    id_restaurante      integer         not null AUTO_INCREMENT,
    name                varchar(100)    not null,
    description         varchar(500)    not null,
    address             varchar(500)    not null,
    image_url           varchar(500)    not null,
    precio_cubiertos    decimal(4,2)    not null default 0.0 check (precio_cubiertos >= 0), 
    PRIMARY KEY (id_restaurante)
);


create table if not exists categorias (
    id_categoria         integer         not null AUTO_INCREMENT,
    nombre_categoria     varchar(100)    not null,
    imagen_categoria varchar(255)    not null,
    PRIMARY KEY (id_categoria)
);


create table if not exists subcategorias_categorias (
    id_categoria         integer         not null,
    id_subcategoria      integer         not null,
    nombre_subcategoria  varchar(100)    not null,
    PRIMARY KEY (id_categoria, id_subcategoria),
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria)
);


create table if not exists item_menu (
    id_item_menu        integer         not null AUTO_INCREMENT,
    id_categoria        integer         not null,
    id_subcategoria     integer         null,
    id_restaurante      integer         not null,
    nombre_item_menu    varchar(100)    not null,
    description         varchar(500)    not null,
    precio              varchar(500)    not null,
    image_url           varchar(500)    null,
    rating              decimal(4,2)    null      check (rate >= 0 and rate <= 5),
    PRIMARY KEY (id_item_menu),
    UNIQUE(id_item_menu, id_restaurante),
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_restaurante) REFERENCES restaurants(id_restaurante)
);

delimiter |
create trigger check_subcategoria_item_menu_on_insert
  before insert on item_menu 
  for each row begin
    if new.id_subcategoria is not null
      then
        if (select count(*) 
          from subcategorias_categorias 
         where id_categoria    = new.id_categoria
           and id_subcategoria = new.id_subcategoria) = 0 
          then
            signal sqlstate '45000';
        end if;
    else
      if (select count(*)
            from subcategorias_categorias 
           where id_categoria = new.id_categoria) > 0 
        then
          signal sqlstate '45000';
      end if;
    end if;
  end
|
delimiter ;

delimiter |
create trigger check_subcategoria_item_menu_on_update
  before update on item_menu 
  for each row begin
    if new.id_subcategoria is not null
      then
        if (select count(*) 
          from subcategorias_categorias 
         where id_categoria    = new.id_categoria
           and id_subcategoria = new.id_subcategoria) = 0 
          then
            signal sqlstate '45000';
        end if;
    else
      if (select count(*)
            from subcategorias_categorias 
           where id_categoria = new.id_categoria) > 0 
        then
          signal sqlstate '45000';
      end if;
    end if;
  end
|
delimiter ;


create table if not exists opciones_item_menu (
    id                  integer         not null AUTO_INCREMENT,
    nombre              varchar(100)    not null,
    PRIMARY KEY (id)
);


create table if not exists detalle_opciones_item_menu (
    id_opciones_item_menu        integer         not null,
    nro_detalle                  integer         not null,
    nombre                       varchar(100)    not null,
    precio                       varchar(10)     null,
    PRIMARY KEY (id_opciones_item_menu, nro_detalle),
    FOREIGN KEY(id_opciones_item_menu) REFERENCES opciones_item_menu(id)
);


create table if not exists item_menu_opciones_item_menu (
    id_item_menu                 integer         not null,
    id_opciones_item_menu        integer         not null,
    PRIMARY KEY (id_item_menu, id_opciones_item_menu),
    FOREIGN KEY(id_item_menu) REFERENCES item_menu(id_item_menu),
    FOREIGN KEY(id_opciones_item_menu) REFERENCES opciones_item_menu(id)
);


create table if not exists usuarios (
    id_usuario          integer         not null AUTO_INCREMENT,
    username            varchar(100)    not null UNIQUE,
    nombre              varchar(50)    not null,
    apellido            varchar(50)    not null,
    email               varchar(100)    not null,
    password            varchar(400)    not null,
    PRIMARY KEY (id_usuario)
);


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


create table if not exists pedidos (
    id_pedidos          integer         not null AUTO_INCREMENT,
    id_usuario          integer         not null,
    id_restaurante      integer         not null,
    id_mesa             integer         not null,
    fecha_hora          timestamp       not null,
    estado              varchar(30)     not null default 'pendiente' check (estado='pendiente' or estado='finalizado'), 
    PRIMARY KEY (id_pedidos),
    UNIQUE(id_pedidos, id_restaurante),
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY(id_restaurante) REFERENCES restaurants(id_restaurante)
);


create table if not exists items_pedido (
    id_item_menu        integer         not null,
    id_pedidos          integer         not null,
    id_restaurante      integer         not null,
    cantidad            integer         not null,
    aclaraciones        varchar(500)    not null,
    PRIMARY KEY (id_item_menu, id_pedidos),
    FOREIGN KEY(id_item_menu, id_restaurante) REFERENCES item_menu(id_item_menu, id_restaurante),
    FOREIGN KEY(id_pedidos, id_restaurante) REFERENCES pedidos(id_pedidos, id_restaurante)
);


create table if not exists opciones_items_pedido (
    id_item_menu          integer         not null,
    id_pedidos            integer         not null,
    id_opciones_item_menu integer       not null,
    nro_detalle           integer       not null,
    PRIMARY KEY (id_item_menu, id_pedidos, id_opciones_item_menu, nro_detalle),
    FOREIGN KEY(id_item_menu, id_pedidos) REFERENCES items_pedido(id_item_menu, id_pedidos),
    FOREIGN KEY(id_opciones_item_menu, nro_detalle) REFERENCES detalle_opciones_item_menu(id_opciones_item_menu, nro_detalle),
    FOREIGN KEY(id_item_menu, id_opciones_item_menu) REFERENCES item_menu_opciones_item_menu(id_item_menu, id_opciones_item_menu)
);


create table if not exists tags (
    id_tag              integer         not null AUTO_INCREMENT,
    nombre              varchar(100)    not null UNIQUE,
    PRIMARY KEY (id_tag)
);


create table if not exists tags_restaurants (
    id_tag              integer         not null,
    id_restaurante      integer         not null,
    PRIMARY KEY (id_tag, id_restaurante),
    FOREIGN KEY(id_tag) REFERENCES tags(id_tag),
    FOREIGN KEY(id_restaurante) REFERENCES restaurants(id_restaurante)
);


create table if not exists managers (
    id_manager          integer         not null AUTO_INCREMENT,
    username            varchar(100)    not null UNIQUE,
    email               varchar(100)    not null,
    id_restaurante      integer         not null,
    password            varchar(400)    not null,
    FOREIGN KEY(id_restaurante) REFERENCES restaurants(id_restaurante),
    PRIMARY KEY (id_manager)
);