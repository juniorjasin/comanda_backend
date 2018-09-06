import unittest
import requests
import json
import sys
from test import Test

class TestCredenciales(Test):

    def test_postPedidoIncorrectBody(self):
        body = '{"incorrect_parameter": 1}'
        response = requests.post("http://localhost:8888/credenciales", body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postNoBody(self):
        response = requests.post("http://localhost:8888/credenciales")
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 400)

    def test_postTokenExpired(self):
        body = '{"username":"andi","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFuZGkiLCJleHAiOjE1MzU1NjU1MjN9.WfbogQuNnXbtc_KhFLTeozeBp5dDihPWgNvFRC4C7coi1yiXWUlGZSGFJ2Sc16CAxLf-4XshJM--lCT58HDYDmzkFXDGvUh80GqQSf_LUx8E59dhqLGXefLcaIRp-iCn6F6yvyuPlDd2Sx89LrbbkpKHb8xoORezyy5ESO-vLuDrnSFS3SBtSwfe9QyGsl_YaPC1WvnROQHFi2QpdVNVdAxr0IHOu8-4wvpI6GLQOqqI5A3412oMk7i-XHQE5-HAZHGrqsuKkxekNcnOT7mysFDs5jkfajz1vedwFvM6F4fiLliFCMeF3sMg1HQgHr2XrVrUmCpWp8KR9qppyXhMP7zPgf2u-lAkB-XJgF7qIRLa27HwJNhq5a6_QQj0tRLzJ8t37GAUwzLK-XKcI5dclU0WTK8NbMDX6cvA7jX6AgvQxwTFLd9j8724hUIfYUoTRnnhnBlEQ9cAwmPhXe-vy7Uz217zV0oBXhiyoICoOOFt0CSGL6WOyan7WypWbVdIs60QlKPszWI1DzuwhqN-Qh6EFHWlhIl518TdrU3I4_YrMXwB6dtlajxp8cjquL2Z61ttoZFseFjRfJgZt3q244jsrAFFBkrchzXhKZdNzR0opECEcVUmIXQ_j8vQXzweGcHFon3Ee32owd9Q78VqDyDXSPJRvsPgfitI10jZmfg"}'
        response = requests.post("http://localhost:8888/credenciales",body)
        content = json.loads(response.content)
        self.assertTrue('token' in content) 
        self.assertEqual(response.status_code, 200)

    def test_postInvalidToken(self):
        body = '{"token":"eyJ0eXAiOiJKV1QiLCJsbGtiOiJSUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFuZGkiLCJleH \
        AiOjE1MzYwOTI4NTR9.z390-YbEkyckw2cGFmmmZ3AXUwqoFQSHTAeQ4oEPGBITAhCU7i_5txFBqqFShrbC7XyN8- \
        b9RIKGfErLR_qNWsGIAI6JJyalAFkM5Ud55rLo2IWzlDX2kD5gfUcRXX6z35rKIN24YE6funO0uQa02PZ0yez9xUjBZ \
        SvByg16L_Li_js2tnQH5uVPm_FclwHULMYdZ7rO5xIWVA6LXJL-oxIPqN0LPl5EZTxpUf-TUIOj6o8eGuVjAggsBhrsW0 \
        ex8zHEo2R8Ido75KO27Kvue5wQh4B3sSWq4TuvOLW59JrjVsM609rfw67cncX_3b_J_7VWHWa6DZzX9P7qDKraHYxFKf2ik \
        YKBxWVzXu-j47Ed8Uu-mC9uSMyPHHQtFQbpFqRgduFLiv8zFp4BVcSmSsOXFzREVFPluRBkPK3Sc6HEwXhIu_CvBazWpyR- \
        GWu8XoTCAGHvOtVO4rkZc8_UvNJ7JjJc1tO4pQs9GF7GnG1ibfS-OqyXC6RDnhk-DCf8Fx5ber858hKoCMnK-USDX3zfm9t \
        2lMZiLnaTexlWYmh5_NwjrKQ_fp59qFD4XWPg9Hys_VyMwxlognx-0Gh81GO405j6h68Pq3fAOpk7zCqgMY5kgdIRkEWbzQ \
        N2P9qLaNc2ioEK_JpQFbU1ZltgDv4W4BhjtP5amMW_cl-xmKE","username":"andi"}'
        response = requests.post("http://localhost:8888/credenciales",body)
        content = json.loads(response.content)
        self.assertTrue('user_message' in content)
        self.assertTrue('code' in content)
        self.assertEqual(response.status_code, 401)

if __name__ == "__main__":
    unittest.main()