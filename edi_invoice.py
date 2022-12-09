# TEST PHP REQUEST GET

import requests
import time


URL = "http://52.163.112.202/rest_b2b/index.php/Edi/export_edi_grn"


def get_req(URL):
    response = requests.get(URL)
    response_data = response.text
    # response_code_get = response.status_code
    # response_data = response.text
    return response_data


start = time.time()
print(get_req(URL))
end = time.time()
print(end - start)