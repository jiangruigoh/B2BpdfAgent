import mysql.connector
import base64
import requests
import time
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
    host="b2b-mysql01.mysql.database.azure.com",
    user="panda_web",
    password=str(base64.b64decode(b'd2ViQGFkbmFw').decode("utf-8")),
    database="lite_b2b",
)

mycursor = mydb.cursor()

mycursor.execute(
    "SELECT a.acc_guid FROM lite_b2b.`acc` a INNER JOIN lite_b2b.acc_settings b ON a.acc_guid = b.customer_guid WHERE b.einv_grab_date IS NOT NULL LIMIT 1")

myresult = mycursor.fetchall()

now = datetime.today().date()
previous_date = now - timedelta(days=1)
previous_2day_date = now - timedelta(days=2)
last_day_month = now - timedelta(days=1)
first_day_month = last_day_month.strftime("%Y-%m-01")
table = ["einv_main","einv_child","ecn_main","ecn_child","consignment_e_invoice_main","consignment_e_invoices"]

#einv_main,einv_child,ecn_main,ecn_child,consignment_e_invoice_main,consignment_e_invoices
#,consignment_e_invoice_main,consignment_e_invoices
# test_now = datetime(2022, 9 , 1).date()
# test_now_1 = test_now - timedelta(days=1)
# print(now.strftime("%d"))
# print(test_now)
# print(test_now_1)
# print(previous_date)
# print(previous_2day_date)
# print(first_day)
# print(now.strftime('%Y-%m-01'))

def get_req(URL):
    response = requests.get(URL)
    response_data = response.text
    # response_code_get = response.status_code
    # response_data = response.text
    return response_data

for x in myresult:

    for y in table: 

        if now.strftime("%d") == "01" :

            URL = f"https://api.xbridge.my/rest_b2b/index.php/Check_compare_data/check_einv_data?start_date={first_day_month}&end_date={last_day_month}&table={y}&customer_guid={x[0]}"

        else :

            URL  = f"https://api.xbridge.my/rest_b2b/index.php/Check_compare_data/check_einv_data?start_date={previous_2day_date}&end_date={previous_date}&table={y}&customer_guid={x[0]}"

# print(URL)

start = time.time()
print(get_req(URL))
end = time.time()
print(end - start)
