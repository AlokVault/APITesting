''' Sending all requests '''
import json
import requests
from csv_json_names import TARGET_NAME, LIST, JSON_DATA, HEADERS,\
    CAMPAIGN_LIST, CAMPAIGN_UPDATE_JSONDATA, \
    TRANSACTION_LIST, TRANSACTION_JSONDATA
from qta import QueryApi
from channel_response_to_csv import ChannelResponseToCsv
from item_response_to_csv_post import ItemResponseCsv1
from wms_response_to_csv_post import WmsResponseToCsv
from campaign_response_to_csv_post import CampaignCreateResponseToCsv

def item_post():
    ''' Adding Items'''
    print("------------- Item  API POST Request Started  -------------- \n \n")
    count = 0
    for item in LIST:
        if "Item" in item:
            with open(JSON_DATA + "\\" + item) as item1:
                json_item = json.load(item1)
                item_data = json.dumps(json_item)

                item_response = requests.post(TARGET_NAME + "items", data=item_data,
                                              auth=('givadmin', 'password'), headers=HEADERS)
                item_response_result = item_response.text
                readresponse = json.loads(item_response_result)
                item_response_detail = readresponse.get("responseDetail")
                item_response_id = item_response_detail.get("responseId")
                item_response_code = item_response_detail.get("responseCode")
                item_transaction_number = readresponse.get("transactionNumber")
                count += 1
                print("Json {0}, ResponeCode = {1} Item {2} with ResponseId {3} "
                      "transactionNumber= {4}".format(item, item_response_code, count,
                                                      item_response_id
                                                      , item_transaction_number))


def item_get():
    '''Getting all the items  '''
    page_no = 0
    item_response = requests.get(TARGET_NAME + "items",  # data=item_data,
                                 auth=('givadmin', 'password'), headers=HEADERS)
    item_response_result = item_response.text
    print(item_response_result)
    dict1 = json.loads(item_response_result)
    totalpages = dict1.get("totalPages")

    if totalpages > page_no:
        item_response1 = requests.get(TARGET_NAME + "items?pageNo=" + str(page_no),
                                      # data=item_data,
                                      auth=('givadmin', 'password'), headers=HEADERS)
        item_response_result1 = item_response1.text
        ItemResponseCsv1().item_response_sent_to_csv1(item_response_result1)
    print("***Item Uploaded and response stored ****** \n \n")


#
# # # #################    WMS    #######################
def wms_post():
    ''' Wms Inventory Add Logic   '''
    print("------------- WMS Inv  API POST Request Started  -------------- \n \n")

    count = 0
    for wms in LIST:
        if "WMS" in wms:  # Put the Json name to search
            with open(JSON_DATA + "\\" + wms) as wms1:
                json_wms = json.load(wms1)
                wms_data = json.dumps(json_wms)
                wms_request = requests.post(TARGET_NAME + "wmsinventory", data=wms_data,
                                            auth=('givadmin', 'password'), headers=HEADERS)
                wms_result = wms_request.text

                WmsResponseToCsv().response_csv(wms_result)
                wms_respose_detail = json.loads(wms_result)

                # Getting the responseId,responseCode and transactionNumber
                wmsresponse_detail = wms_respose_detail.get("responseDetail")
                wms_response_id = wmsresponse_detail.get("responseId")
                wms_response_code = wmsresponse_detail.get("responseCode")

                count += 1
                print(
                    "***Overall WMS ResponeCode = {0} Item {1} with ResponseId {2} "
                    "json = {3}".format(wms_response_code,
                                        count,
                                        wms_response_id,
                                        wms))
    # QTA sending request
    QueryApi().query_transaction_tansactions_qta()

    # QIA sending request
    QueryApi().query_inventory_details_qia()

    print("WMS Uploaded and response stored  \n \n  ")


# # # ######################## CampaignCreate  Create ########################3
def campaign_create():
    '''  Campaign Create Request '''
    print("------------- Campaign Create API POST Request Started  -------------- \n \n")

    for campaign in LIST:
        count = 0
        if "Campaign" in campaign:
            with open(JSON_DATA + "\\" + campaign) as campaign1:
                json_campaign = json.load(campaign1)
                campaign_data = json.dumps(json_campaign)
                campaign_request = requests.post(TARGET_NAME + "campaigns", data=campaign_data,
                                                 auth=('givadmin', 'password'), headers=HEADERS)
                campaign_result = campaign_request.text

                # Storing the resposeId,responseCode
                campaign_response_result = json.loads(campaign_result)
                campaign_response_detail = campaign_response_result.get("responseDetail")
                campaign_response_id = campaign_response_detail.get("responseId")
                campaign_response_code = campaign_response_detail.get("responseCode")

                # Storing the Post request response
                CampaignCreateResponseToCsv().campaign_response_csv(campaign_result)
                print("***Overall CampaignCreate ResponeCode = {0} Item {1} with "
                      "ResponseId {2} json = {3}".format(campaign_response_code,
                                                         count, campaign_response_id, campaign))
                count += 1

    # QTA sending request
    QueryApi().query_transaction_tansactions_qta()
    #
    # QIA sending request
    QueryApi().query_inventory_details_qia()
    print("CampaignCreated and Updates Done and response stored   \n \n")


################################  Campaign Update #############################
def campaign_update():
    ''' Campaign Update logic '''
    print("------------- Campaign Update  API POST Request Started  -------------- \n \n")

    for update in CAMPAIGN_LIST:
        count = 0
        if "Campaign" in update:
            with open(CAMPAIGN_UPDATE_JSONDATA + "\\" + update) as update_campaign:
                json_update_campaign = json.load(update_campaign)
                update_campaign_data = json.dumps(json_update_campaign)
                update_campaign_request = requests.post(TARGET_NAME + "campaigns",
                                                        data=update_campaign_data,
                                                        auth=('givadmin', 'password'),
                                                        headers=HEADERS)
                update_campaign_result = update_campaign_request.text

                # Storing the resposeId,responseCode
                update_campaign_response_result = json.loads(update_campaign_result)
                update_campaign_response_detail = update_campaign_response_result. \
                    get("responseDetail")
                update_campaign_response_id = update_campaign_response_detail.get("responseId")
                update_campaign_response_code = update_campaign_response_detail.get("responseCode")

                # Storing the Post request response
                CampaignCreateResponseToCsv().campaign_response_csv(update_campaign_result)
                print("***Overall Campaign Update ResponeCode = {0} Item {1} with"
                      " ResponseId {2} json = {3}".format(
                          update_campaign_response_code, count,
                          update_campaign_response_id, update))
                count += 1

    # QTA sending request
    QueryApi().query_transaction_tansactions_qta()
    #
    # QIA sending request
    QueryApi().query_inventory_details_qia()
    print("Campaign Update and Updates Done and response stored \n \n")


def transaction_post():
    '''' All Transaction Calls'''
    count = 0
    print("-------------Channel call started-------------- \n \n")
    for transactions in TRANSACTION_LIST:
        """ Channel Transaction """
        if "trans"  in transactions:
            with open(TRANSACTION_JSONDATA + "\\" + transactions) as channel:
                json_channel = json.load(channel)
                channel_data = json.dumps((json_channel))
                if "shipDate" in channel_data:
                    channel_result = requests.post(TARGET_NAME + "channel", data=channel_data,
                                                   auth=('givadmin', 'password'), headers=HEADERS)
                    channel_response_result = channel_result.text
                    ChannelResponseToCsv().channel_response_csv(channel_response_result)

                    # Storing the resposeId,responseCode
                    channel_response_result = json.loads(channel_response_result)
                    channel_response_detail = channel_response_result.get("responseDetail")
                    channel_response_id = channel_response_detail.get("responseId")
                    channel_response_code = channel_response_detail.get("responseCode")
                    print("*** Overall Channel ResponeCode = {0} Item {1} with"
                          " ResponseId {2} json = {3} \n".format(
                              channel_response_code,
                              count,
                              channel_response_id, transactions))
                    count += 1
                    # if count > 12:
                    #     break
                elif "campaignStartDate" in channel_data:
                    """ Campaign Transaction """
                    campaign_result = requests.post(TARGET_NAME + "campaigns", data=channel_data,
                                                    auth=('givadmin', 'password'), headers=HEADERS)
                    campaign_response_result = campaign_result.text
                    # Storing the resposeId,responseCode
                    CampaignCreateResponseToCsv().campaign_response_csv(campaign_response_result)
                    campaign_response_detail = json.loads(campaign_response_result)
                    campaign_response_detail = campaign_response_detail.get("responseDetail")
                    campaign_response_id = campaign_response_detail.get("responseId")
                    campaign_response_code = campaign_response_detail.get("responseCode")
                    print("*** Overall Campaign ResponeCode = {0} Item {1} with ResponseId {2} "
                          "json = {3} \n".format(
                              campaign_response_code,
                              count,
                              campaign_response_id, transactions))
                    count += 1


                if "serialNumber" in channel_data:
                    """ Wms Invtory Transaction """
                    inv_response_request = requests.post(TARGET_NAME + "wmsinventory",
                                                         data=channel_data,
                                                         auth=('givadmin', 'password'),
                                                         headers=HEADERS)
                    inv_response_result = inv_response_request.text
                    WmsResponseToCsv().response_csv(inv_response_result)

                    # Storing the resposeId,responseCode
                    inv_trnx_response_result = json.loads(inv_response_result)
                    inv_trnx_response_detail = inv_trnx_response_result.get("responseDetail")
                    inv_trnx_response_id = inv_trnx_response_detail.get("responseId")
                    inv_trnx_response_code = inv_trnx_response_detail.get("responseCode")

                    print(
                        "*** Overall Wms Transactions ResponeCode = {0} Item {1} with "
                        "ResponseId {2} json = {3} \n".format(
                            inv_trnx_response_code,
                            count,
                            inv_trnx_response_id, transactions))
                    count += 1


    # QTA sending request
    QueryApi().query_transaction_tansactions_qta()

    # QIA sending request
    QueryApi().query_inventory_details_qia()
    print("Transaction Call Done and response stored \n \n")
