# get restaurantes
curl -v -X GET 'http://localhost:8888/restaurantes' | python -m json.tool

### Server 
curl -v -X GET 'http://34.230.44.202:8888/restaurantes' | python -m json.tool

# login
curl -v -X POST -d '{"user":{"username":"andresbalestrini", "password":"andi"}}' 'http://localhost:8888/login' | python -m json.tool

### Sever
curl -v -X POST -d '{"user":{"username":"jrjs", "password":"jrjs"}}' 'http://34.230.44.202:8888/login' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"andi", "password":"andi"}}' 'http://34.230.44.202:8888/login' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"juan", "password":"juan"}}' 'http://34.230.44.202:8888/login' | python -m json.tool

# post consulta menu
curl -v -H "Content-Type: application/json" -X POST -d '{"id_restaurante":1}' 'http://localhost:8888/asd/menu' | python -m json.tool

### Sever
curl -v -H "Content-Type: application/json" -X POST -d '{"id_restaurante":1}' 'http://34.230.44.202:8888/asd/menu' | python -m json.tool

# post insertar orden
curl -v -H "Content-Type: application/json" -X POST -d '
{"order":{"id_restaurante":1, "id_mesa":1, items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}' 'http://localhost:8888/asd/pedido' | python -m json.tool

### Sever
curl -v -H "Content-Type: application/json" -X POST -d '
{"order":{"id_restaurante":1, "id_mesa":1, "items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}' 'http://34.230.44.202:8888/asd/pedido' | python -m json.tool


# post registrar
curl -v -X POST -d '{"user":{"username":"andresbalestrini", "password":"andi","email":"algo@gmail.com"}}' 'http://localhost:8888/register' | python -m json.tool

### Sever
curl -v -X POST -d '{"user":{"username":"jrjs", "password":"jrjs","email":"jrjs@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"andi", "password":"andi","email":"andi@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"juan", "password":"juan","email":"juan@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool