import mysql.connector
import requests
import time
import datetime
import base64


mydb = mysql.connector.connect(
    host="b2b-mysql01.mysql.database.azure.com",
    user="panda_web",
    password=str(base64.b64decode(b'd2ViQGFkbmFw').decode("utf-8")),
    database="lite_b2b",
)

mycursor = mydb.cursor()

mycursor.execute(
    "SELECT a.acc_guid FROM lite_b2b.acc AS a WHERE a.isactive = '1' AND a.trial_mode = '0'")

myresult = mycursor.fetchall()

period_code = datetime.datetime.now()


def get_req(URL):
    response = requests.get(URL)
    response_data = response.text
    # response_code_get = response.status_code
    # response_data = response.text
    return response_data


for x in myresult:

    URL = f"https://api.xbridge.my/rest_b2b/index.php/Check_compare_data/generate_daily_report?period_code={period_code.strftime('%Y-%m')}&customer_guid={x[0]}"

    start = time.time()
    print(get_req(URL))
    end = time.time()
    print(end - start)
