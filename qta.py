''' Logic for Query API '''
import json
import requests
from csv_json_names import TARGET_NAME
from query_response import QueryResponseToCsv

HEADERS = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json"}


class QueryApi():
    ''' Query Api class'''
    def query_inventory_details_qia(self):
        ''' Query Inventory Details '''
        qia = {
            "action": "QIA",
            "inventorySource": "G"
        }
        qia_josn = json.dumps(qia)
        qia_response = requests.post(TARGET_NAME + "QueryInventoryDetails", data=qia_josn,
                                     auth=('givadmin', 'password'), headers=HEADERS)
        qia_response_result1 = qia_response.text
        # QTA storing response to excel file
        QueryResponseToCsv().qia_query(qia_response_result1)

    def query_transaction_tansactions_qta(self):
        ''' Query Inventory Details '''

        qta_p = {
            "fromTimeStamp": "2020-01-01T05:21:00.000",
            "action": "QTA",
            "requestFor": "P",
            "inventorySource": "G"
        }
        qta_a = {
            "fromTimeStamp": "2020-01-01T05:21:00.000",
            "action": "QTA",
            "requestFor": "A",
            "inventorySource": "G"
        }
        qta_p_json = json.dumps(qta_p)
        qta_a_json = json.dumps(qta_a)
        qta_response_p = requests.post(TARGET_NAME + "QueryInventoryTransactions",
                                       data=qta_p_json,
                                       auth=('givadmin', 'password'), headers=HEADERS)
        qta_response_a = requests.post(TARGET_NAME + "QueryInventoryTransactions",
                                       data=qta_a_json,
                                       auth=('givadmin', 'password'), headers=HEADERS)
        qta_response_protect = qta_response_p.text
        QueryResponseToCsv().qta_query_protect(qta_response_protect)

        qta_response_allocate = qta_response_a.text
        # QTA storing response to excel file
        QueryResponseToCsv().qta_query_allocate(qta_response_allocate)
