# Send Reminder Renewal Script
# 0 2 * * * /media/estore/fastAPI/B2BpdfAgent/env/bin/python3.8 /media/estore/fastAPI/B2BpdfAgent/reminder_renewal.py > /media/estore/fastAPI/B2BpdfAgent/log/reminder_renewal.log

import requests
import time


URL = "https://api.xbridge.my/rest_b2b/index.php/Reminder_renewal/S_reminder_renewal/"


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