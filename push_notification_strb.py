# TEST PHP REQUEST GET

import requests
import time


URL = "https://api.xbridge.my/rest_b2b/index.php/B2b_backend_process/check_strb_accept/"


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

URL2 = "https://api.xbridge.my/rest_b2b/index.php/B2b_backend_process/check_pending_e_invoice/"


start = time.time()
print(get_req(URL2))
end = time.time()
print(end - start)
