# TEST PHP REQUEST GET

import requests
import time


URL = "https://api.xbridge.my/rest_b2b/index.php/Get_pending_document/"


def get_req(URL):
    response = requests.get(URL, params={"uploaded_status": "0",
                                         "uploaded_status_strb": "0",
                                         "tf_uploaded_status": "99",
                                         "tf_uploaded_status_strb": "0",
                                         })
    response_data = response.text
    # response_code_get = response.status_code
    # response_data = response.text
    return response_data


start = time.time()
print(get_req(URL))
end = time.time()
print(end - start)
