INSERT INTO restaurants (name, description, address, image_url, precio_cubiertos)
VALUES ('La Mamma', 'Restaurante', 'Av. Rafael Núñez 6092, 5021 Córdoba', 'http://34.230.44.202:8888/images/1-lamamma_logo4.jpg', 35.00);

INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Antipasti Freddi", "https://image.flaticon.com/icons/svg/174/174381.svg"); 
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Antipasti Caldi", "https://image.flaticon.com/icons/svg/174/174378.svg"); 
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Pasta Secca De Cecco", "https://image.flaticon.com/icons/svg/701/701980.svg"); 
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Le lasagne La Mamma", "https://image.flaticon.com/icons/svg/468/468631.svg"); 
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("La Pasta Fatta in Casa La Mamma", "https://image.flaticon.com/icons/svg/701/701980.svg"); 
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Pasta Ripiena La Mamma", "https://image.flaticon.com/icons/svg/701/701980.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Risotti  La  Mamma", "https://image.flaticon.com/icons/svg/94/94322.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Carni Alla Griglia", "https://image.flaticon.com/icons/svg/80/80298.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Spiedini  La  Mamma", "https://image.flaticon.com/icons/svg/933/933286.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Frutti  Di  Mare", "https://image.flaticon.com/icons/svg/701/701976.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Carni Bianche", "https://image.flaticon.com/icons/svg/933/933310.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Carni Rosse", "https://image.flaticon.com/icons/svg/933/933310.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Insalate", "https://image.flaticon.com/icons/svg/701/701974.svg");
INSERT INTO categorias (nombre_categoria, imagen_categoria) VALUES ("Zuppe", "https://image.flaticon.com/icons/svg/203/203811.svg");


INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Salami di Oncativo","Salami di Oncativo", "130", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "La Mamma Pomodori Secchi","Tomates secos, aceite de oliva y láminas de ajo", "135", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Peperoni Arrostiti","Pimientos asados con aceite de oliva y láminas de ajo", "135", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Vitello Tonnato","El clásico, salsa vithel y alcaparras", "150", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Caponatta","El clásico antipasto italiano", "135", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Carpaccio di Salmone Affumicato","Acompañado de queso blanco y alcaparras", "320", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Burrata Di Bufalla  (per tre persone)","Pulpeta rellena con crema, acompañada de  rúcula, jamón crudo, tomates secos, olivas negras, aceite de oliva y  pimienta negra", "390", null);
-- INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
-- VALUES (1, 1, "Mozzarella Treccia  (per tre persone)","Trenzada con rúcula, jamón crudo, tomates secos, olivas negras, aceite de oliva y  pimienta negra", "", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Tavolo Congiunto (per tre persone)","Jamón crudo de Parma, salame de Oncativo, mortadela italiana con pistacho, Jamón cocido seleccionado, queso Brie, gouda, brind amoure", "580", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (1, 1, "Tavolo Patagonica  (per tre persone)","Jamón de jabalí, jamón de ciervo, salmón ahumado, queso ahumado y arrollado de queso especial, con queso crema, alcaparras y almendras", "650", null);


INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 1, "Mozzarella in Carrozza","Romana come il Colloseo", "195", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 1, "Crepps De Otros Tiempos","Finos crepps al huevo, con champignon salteados en manteca, mozzarella y Pimienta negra", "180", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (2, 1, "Seppie e Zuccini alla Romana","Las clásicas rabas y zuccini a la romana", "230", null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Spaghetti Al Profumo Di  Limone","Con panceta ahumada, crema, vodka y ralladura de limón, verdaderamente espectaculares", "275", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Penne Rigate  All’arrabbiata","Tomate, ajo, peperonccino, albahaca, bien picante", "285", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Pappardelle All’amatriciana","Manteca, panceta ahumada, vino blanco y tomate", "290", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (3, 1, "Pappardelle Strogonoff","Cintas de lomo, crema, champignones y parmigiano", "290", null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (4, 1, "Lasagna Di Pollo E Verdure","pollo grillado, espinaca y parmesano", "300", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (4, 1, "Lasagna Di Verdure","berenjena, champiñón, zanahoria, zuchinni, salteado en oliva, ricota, con tomate fresco y lluvia de almendras", "300", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (4, 1, "Lasagna Verde","Masa de espinacas, rellena de carne y suave salsa bechamel", "300", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (4, 1, "Lasagna Alla Marsala","Marsala Y Champiñones", "320", null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (4, 1, "Lasagna Del Mare","Salmón rosado, ricota, bechamel acompañada con salsa del marinero, crema, camarones, mejillones y berberechos", "450", null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Gnocchi  Di Patate Alla Cacciatora","Tomate, pollo y romero", "290",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Tagliatelle A Modo Mio","Crema, panceta ahumada, yema de huevo y  pimienta negra", "290",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Fettuccine Delicious","Crema, blanco de ave al coñac y champiñones", "295",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Tagliatelle Frutti Di Mare","Pomodoro, ajo, vino blanco, salmón rosado, mariscos y perejil", "410",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Sorrentini Nero Di Seppia","Relleno con trucha y salmón ahumado, con oliva, tomate concasse, Almendras tostadas y menta fresca", "290",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (5, 1, "Fussilli Al Fierrito","con salsa Scarparo, verdeo, pomodoro, parmesano y pesto", "300",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Cannelloni Alla Rossini","los invento el gran músico", "270",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Cannelloni Alla Piemontese","Crema y ragu", "270",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Trittico","ravioles de lomo y hongos, ñoquis y sorrentinos, en sus salsas", "330",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Ravioli","de lomo, hongos y queso azul", "330",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Ravioli"," verdes de mousse de espinacas", "330",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Sorrentini","de jamón, mozzarella y nueces", "330",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (6, 1, "Cappelletti","de pollo, jamón crudo y cerdo", "330",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (7, 1, "Risotto Rosso","Pollo, panceta ahumada, hongos secos, champiñón, perfumado con pimentón", "310",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (7, 1, "Risotto Zaferano","azafranado con mejillones, berberechos, cayos de vieras, langostinos y perejil", "350",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 1, "Paillard de lomo","200 grs", "360",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 1, "Medallon de lomo","250 grs", "410",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 1, "Tournedo de lomo","300 grs", "420",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 1, "Entrecotte","300 grs", "420",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (8, 1, "Bife de chorizo","400 grs", "420",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (9, 1, "Spiedino di filetto","De lomo, acompañado de papas españolas", "400",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (9, 1, "Spiedino Misto","lomo, pollo y cerdo. Acompañado de papas españolas", "400",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Merluzzo Romano Con Puré","Merluza a la romana con puré", "270",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Salmone All’ Uso Nostro","Grillado sobre papas panaderas, cocinadas al horno con cebollas y pimientos,  delicada salsa de yemas, Marsala, perejil  y pimentón", "550",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Pacifico Salmone Alla Griglia","Salmón rosado acompañado de Cous–cous", "550",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (10, 1, "Pacú Con Verduras Grilladas","Pacú Con Verduras Grilladas", "400",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Cosce Di Pollo Con Mix De Verdes","Cosce Di Pollo Con Mix De Verdes", "310",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Petto Di Pollo Alla Crema Di Limone","Pechuguitas, acompañadas con puré de papas", "310",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Disossato Soubisse","Deshuesado, relleno de loncha panceta ahumada, mozzarella y olivas negras, Acompañado de puré de papas", "370",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Disossato  All’estragone","Dados de pollo saltados a la manteca, crema, coñac y champiñones acompañado de arroz blanco con manteca y queso", "370",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (11, 1, "Disossato  Raffaele","Deshuesado agridulce, ananá, crema y toque de salsa caramelo", "370",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Cubetti di filetto alla calabrese","Dados de lomo a la calabresa", "370",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Picattini Di Sofia Loren","Tiernos bifecitos de lomo cocinados con manteca y limón", "360",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Bistecca Di Filetto En Reducción De Malbec­­","Medallones de lomo con papas y brócolis gratinados", "390",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Matambre De Cerdo","A la parrilla acompañado de papas fritas", "395",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Controfiletto Hongroisse","(Entrecote, crema, hongos, pimentón y brócolis parmesana)", "380",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Filetto Al Pepe Nero","Lomo a la pimienta negra y papas a la crema", "450",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Filetto Gruyere","Lomo grillado relleno con morron asado y queso gruyere derretido con guarnicion a eleccion…", "450",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Filetto Patagónico","Medallones de lomo salteados en oliva, crema de jamón de ciervo ahumado, y queso de cabra, acompañado de fritata de vegetales", "450",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (12, 1, "Filetto Bla Blay","Envuelto en panceta ahumada, con champiñon, cebolla al whisky, demi glace, acompañado de tomates a la italiana", "450",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Sempre  Quelle  Della  Vostra  Scelta","Lechuga, crespa o mantecosa, rúcula todas hidropónicas, achicoria, brócoli, Remolachas cocidas, apio, aceitunas, choclo, zanahoria, papas, huevo duro", "110",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Light","Tomate, queso magro y albahaca 170 cal. la porción", "190",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Miranda","Tomate, huevo, lechuga, apio, remolacha, atún, aceitunas y anchoas", "220",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Portofino","Salmón rosado grillado, croutones, gruyere y mix de verdes", "320",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (13, 1, "Cesar","Il classico", "320",null);

INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (14, 1, "Di Zucchine Con Aglio","La clásica sopa argentina", "150",null);
INSERT INTO item_menu (id_categoria, id_restaurante, nombre_item_menu, description, precio, image_url)
VALUES (14, 1, "Cappelleti In  Brodo","La sopa navideña italiana por excelencia", "240",null);