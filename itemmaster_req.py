# ITEMMASTER

"""
Version No: 1
Release Date: 23 November 2021 
KKSC
"""
from json2html import *
from timeit import default_timer as timer
from func_helper.post_models import raw_itemmaster_mdl
from tqdm import tqdm
from concurrent.futures import as_completed

from func_helper.request_func import post_django, create_ticket
from func_helper.error_decorator import *


class HelpDesk_msg(object):
    def __init__(self):
        # HELPDESK MESSAGE
        self.helpdesk_message_list = []
        self.json_msg_lst = { "B2B NO ITEMMASTER data": self.helpdesk_message_list }

    def __repr__(self) -> str:
        return super().__repr__()

main_message = HelpDesk_msg()

@general_error_handler
def main_itemmaster_request(itemmaster_post_url, plodas, session_req_get):
    """
    # GET/POST/PATCH 
    """
    post_model = raw_itemmaster_mdl(plodas["customer_guid"], plodas["vendor_code"],\
        plodas["Itemcode"], plodas["Barcode"], plodas["ArticleNo"], plodas["Description"],\
        plodas["UM"], plodas["ItemLink"], plodas["import_at"])
    # print(post_model)
    post_response = post_django(itemmaster_post_url, post_model, session_req_get)
    return {"post_response": post_response}

@concurrency_err
def job_ticket_checkpoint(jobs):
    with  tqdm(total=len(jobs),  desc="Running Jobs") as progress:
            for out in as_completed(jobs):
                json_info = out.result()
                # print(out)
                progress.update(1)
                #print(json_info)
                # results = [r.result() for r in jobs]
                # print(results)
                s
    if len(main_message.helpdesk_message_list) != 0:
        #print("CREATING A TICKET...")
        company_guid = "BFBC7669C97411E9AFB1DED0BD1483FD"
        outlet_code = "B2B"
        dic_html_msg = json2html.convert(json = main_message.json_msg_lst)
        create_ticket(company_guid, outlet_code, dic_html_msg)
        print("TICKET CREATED...")
    else:
        print("ALL ITEMMASTER HAVE DATA")
    return "Ticket Checkpoint"

@general_error_handler
def general_multi_itemmaster(itemmaster_post_url, data, session_req_get):
    start = timer()
    with concurrent.futures.ThreadPoolExecutor() as executor: # optimally defined number of threads
        jobs = [ executor.submit( main_itemmaster_request, itemmaster_post_url, i, session_req_get) for i in data ]
        print('THREADS USED:', len(executor._threads))
        print('pending:', executor._work_queue.qsize(), 'jobs')
        job_ticket_checkpoint(jobs)
    
    end = timer()
    print(end - start) # Time in seconds, e.g. 5.38091952400282
    return "Processs End"