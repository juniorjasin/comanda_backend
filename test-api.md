# get restaurantes
curl -v -X GET 'http://localhost:8888/restaurantes' | python -m json.tool

### Server 
curl -v -X GET 'http://34.230.44.202:8888/restaurantes' | python -m json.tool

# login
curl -v -X POST -d '{"user":{"username":"andi", "password":"andi"}}' 'http://localhost:8888/login' | python -m json.tool

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
{"order":{"id_restaurante":1, "id_mesa":1, "items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}' 'http://localhost:8888/asd/pedido' | python -m json.tool

curl -v -H "Content-Type: application/json" -H "Authorization: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFuZGkiLCJleHAiOjE1MzU1NjU1MjN9.WfbogQuNnXbtc_KhFLTeozeBp5dDihPWgNvFRC4C7coi1yiXWUlGZSGFJ2Sc16CAxLf-4XshJM--lCT58HDYDmzkFXDGvUh80GqQSf_LUx8E59dhqLGXefLcaIRp-iCn6F6yvyuPlDd2Sx89LrbbkpKHb8xoORezyy5ESO-vLuDrnSFS3SBtSwfe9QyGsl_YaPC1WvnROQHFi2QpdVNVdAxr0IHOu8-4wvpI6GLQOqqI5A3412oMk7i-XHQE5-HAZHGrqsuKkxekNcnOT7mysFDs5jkfajz1vedwFvM6F4fiLliFCMeF3sMg1HQgHr2XrVrUmCpWp8KR9qppyXhMP7zPgf2u-lAkB-XJgF7qIRLa27HwJNhq5a6_QQj0tRLzJ8t37GAUwzLK-XKcI5dclU0WTK8NbMDX6cvA7jX6AgvQxwTFLd9j8724hUIfYUoTRnnhnBlEQ9cAwmPhXe-vy7Uz217zV0oBXhiyoICoOOFt0CSGL6WOyan7WypWbVdIs60QlKPszWI1DzuwhqN-Qh6EFHWlhIl518TdrU3I4_YrMXwB6dtlajxp8cjquL2Z61ttoZFseFjRfJgZt3q244jsrAFFBkrchzXhKZdNzR0opECEcVUmIXQ_j8vQXzweGcHFon3Ee32owd9Q78VqDyDXSPJRvsPgfitI10jZmfg" -X POST -d '
{"order":{"id_restaurante":1,"id_mesa":3, "items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}' 'http://localhost:8888/asd/pedido' | python -m json.tool

### Sever
curl -v -H "Content-Type: application/json" -X POST -d '
{"order":{"id_restaurante":1, "id_mesa":1, "items":[{"id":"1","cantidad": 3,"aclaraciones": "sin ajo"},{"id":"2","cantidad": 1,"aclaraciones": "sin queso"}]}}' 'http://34.230.44.202:8888/asd/pedido' | python -m json.tool


# post registrar
curl -v -X POST -d '{"user":{"username":"andresbalestrini", "password":"andi","email":"algo@gmail.com"}}' 'http://localhost:8888/register' | python -m json.tool

### Sever
curl -v -X POST -d '{"user":{"username":"jrjs", "password":"jrjs","email":"jrjs@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"andi", "password":"andi","email":"andi@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool

curl -v -X POST -d '{"user":{"username":"juan", "password":"juan","email":"juan@gmail.com"}}' 'http://34.230.44.202:8888/register' | python -m json.tool

# Credenciales
curl -v -X POST -d '{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFuZGkiLCJleHAiOjE1MzYwOTI4NTR9.z390-YbEkyckw2cGFmmmZ3AXUwqoFQSHTAeQ4oEPGBITAhCU7i_5txFBqqFShrbC7XyN8-b9RIKGfErLR_qNWsGIAI6JJyalAFkM5Ud55rLo2IWzlDX2kD5gfUcRXX6z35rKIN24YE6funO0uQa02PZ0yez9xUjBZSvByg16L_Li_js2tnQH5uVPm_FclwHULMYdZ7rO5xIWVA6LXJL-oxIPqN0LPl5EZTxpUf-TUIOj6o8eGuVjAggsBhrsW0ex8zHEo2R8Ido75KO27Kvue5wQh4B3sSWq4TuvOLW59JrjVsM609rfw67cncX_3b_J_7VWHWa6DZzX9P7qDKraHYxFKf2ikYKBxWVzXu-j47Ed8Uu-mC9uSMyPHHQtFQbpFqRgduFLiv8zFp4BVcSmSsOXFzREVFPluRBkPK3Sc6HEwXhIu_CvBazWpyR-GWu8XoTCAGHvOtVO4rkZc8_UvNJ7JjJc1tO4pQs9GF7GnG1ibfS-OqyXC6RDnhk-DCf8Fx5ber858hKoCMnK-USDX3zfm9t2lMZiLnaTexlWYmh5_NwjrKQ_fp59qFD4XWPg9Hys_VyMwxlognx-0Gh81GO405j6h68Pq3fAOpk7zCqgMY5kgdIRkEWbzQN2P9qLaNc2ioEK_JpQFbU1ZltgDv4W4BhjtP5amMW_cl-xmKE","username":"andi"}' 'http://localhost:8888/credenciales' | python -m json.tool


# Managers
curl -v -X POST -d '{"user":{"username":"andi", "password":"andi"}}' 'http://localhost:8888/manager' | python -m json.tool