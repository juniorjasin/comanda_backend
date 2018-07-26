# get restaurantes
curl -v -X GET 'http://localhost:8888/restaurantes' | python -m json.tool

# login
curl -v -X GET 'http://localhost:8888/login' | python -m json.tool

# post consulta menu
curl -v -H "Content-Type: application/json" -X POST -d '{"id_restaurante":1}' 'http://localhost:8888/asd/menu' | python -m json.tool