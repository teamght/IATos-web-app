import requests
import json
from .util import ENDPOINT_TENSORFLOW_MODEL


def get_result_from_model(tos):
    b64_str = tos
    
    PARAMS = {'data': b64_str}
    response = requests.post(url=ENDPOINT_TENSORFLOW_MODEL,data=PARAMS)
    print('Respuesta de la red neuronal: {}'.format(response.text))
    predictions = json.loads(response.text)

    return f'{predictions}'


if __name__ == '__main__':
    get_result_from_model('')
