import logging
import json
import os
import python_jwt as jwt
import Crypto.PublicKey.RSA as RSA

logger = logging.getLogger('decorator')
logger.setLevel(logging.DEBUG)
logger.propagate = False
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

public_key_file = os.path.join(os.environ['INSTALL_DIR'], 'keys','byewaitKeyy.pub')
with open(public_key_file, 'r') as fd:
    public_key = RSA.importKey(fd.read())

def check_authentication(f):
    def wrapper(*args):
        logger.debug('check_authentication decorator')
        request = args[0].request
        data = json.loads(request.body)
        token = data['token']
        logger.debug(data)
        
        try:
            header, claims = jwt.verify_jwt(token, public_key,['RS256'])
            logger.debug(claims)
            logger.debug(claims['userName'])
        except Exception as ex:
            logger.debug("Error: {0}".format(ex))
            raise Exception
        

        return f(*args)
    return wrapper