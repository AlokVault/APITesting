import os

TARGET_NAME = "http://s3demo1.eastus.cloudapp.azure.com:8443/api/"
TARGET_NAME_SCRIPT = "s3demo1.eastus.cloudapp.azure.com"
'''   ITEM    '''

CSV_FOR_ITEM = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\My_own_item.csv'
JSONNAME_FOR_ITEM = "D:/GIV/givtrans_api_automation/calculationJson/Item"
SCRIPTNAME_FOR_ITEM = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\item.bat'
ITEM_RESPONSE_FILE = 'D:\\GIV\\givtrans_api_automation\\Response_File\\item_response_result.csv'
'''  WMS Inventory  '''

CSV_FOR_WMS = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\WMSInventory.xlsx'
JSONNAME_FOR_WMS = 'D:\\GIV\\givtrans_api_automation\\calculationJson\\WMS.json'
SCRIPTNAME_FOR_WMS = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\wms.bat'
WMS_RESPONSE_FILE = 'D:\\GIV\\givtrans_api_automation\\Response_File\\wms_response_result.csv'

'''    CampaignCreate Create   '''

CAMPAIGN_CREATE_LIST = os.listdir('D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\CampaignCreate')
CSV_FOR_CAMPAIGN_CREATE = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\CampaignCreate'
JSONNAME_FOR_CAMPAIGN_CREATE = "D:\\GIV\\givtrans_api_automation\\calculationJson\\CampaignCreate"
SCRIPTNAME_FOR_CAMPAIGN_CREATE = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\campaignCreate.sh'
CAMPAIGN_RESPONSE_FILE = 'D:\\GIV\\givtrans_api_automation\\Response_File\\campaign_response_result.csv'

'''   CampaignCreate Header Update    '''

CSV_FOR_CAMPAIGN_HEADER_UPDATE = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\' \
                                 'Campaign_Header_No_data_update.csv'
JSONNAME_FOR_CAMPAIGN_HEADER_UPDATE = 'D:\\GIV\\givtrans_api_automation\\calculationJson\\Update_Camp'\
                                      '\\CampaignUpdate'
SCRIPTNAME_FOR_CAMPAIGN_HEADER_UPDATE = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\' \
                                        'campaignHeaderUpate.sh'

'''  CampaignCreate Details Update '''
CSV_FOR_CAMPAIGN_DETAIL_UPDATE = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\' \
                                 'Campaing_Update_with_Data12.xlsx'
JSONNAME_FOR_CAMPAIGN_DETAIL_UPDATE = 'D:\\GIV\\givtrans_api_automation\\calculationJson\\Update_Camp\\'\
                                      'Campaign_Update_07.json'
SCRIPTNAME_FOR_CAMPAIGN_DETAIL_UPDATE = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\' \
                                        'campaignDataUpate.sh'


''' Transaction '''
SCRIPTNAME_FOR_TRANSACTION = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\Transaction.bat'
SCRIPTNAME_FOR_WMS_TRANSACTION = 'D:\\GIV\\givtrans_api_automation\\calculation_script\\channelTransaction.sh'
CHANNEL_RESPONSE_FILE = 'D:\\GIV\\givtrans_api_automation\\Response_File\\channel_response_result.csv'

'''Details for Script file'''

USERNAME = 'givadmin'
PASSWORD = 'password'
WMS_APINAME = 'wmsinventory'
ITEM_APINAME = 'items'
CAMPAIGN_APINAME = "campaigns"
CHANNEL_APINAME = 'channel'


''' Send Request File Parameter'''

HEADERS = {"Content-Type": "application/json;charset=UTF-8", "Accept": "application/json"}
LIST = os.listdir("D:\\GIV\\givtrans_api_automation\\calculationJson")
CAMPAIGN_LIST = os.listdir("D:\\GIV\\givtrans_api_automation\\calculationJson/Update_Camp")
CAMPAIGN_UPDATE_JSONDATA = "D:\\GIV\\givtrans_api_automation\\calculationJson\\Update_Camp"
JSON_DATA = "D:\\GIV\\givtrans_api_automation\\calculationJson"
TRANSACTION_LIST = os.listdir('D:\\GIV\\givtrans_api_automation/calculationJson/Transaction')
TRANSACTION_JSONDATA = "D:\\GIV\\givtrans_api_automation\\calculationJson\\Transaction"
WMS_TRANSACTION_JSONDATA = "D:\\GIV\\givtrans_api_automation\\calculationJson\\Wms_inventory_Transaction"

'''  Transaction File Variables '''
TRANSACTION_CSV_LIST = os.listdir('D:/GIV/givtrans_api_automation/Calculation_CSV/Trnx')
CHANNEL_TRANSACTION_CSV = 'D:\\GIV\\givtrans_api_automation\\Calculation_CSV\\Trnx'
JSONNAME_FOR_CHANNEL_TRANSACTION = 'D:\\GIV\\givtrans_api_automation\\calculationJson\\Transaction\\trans'
SCRIPTFILE_TRANSACTION = open(SCRIPTNAME_FOR_TRANSACTION, "w")

'''  Query CSv Files'''
QTA_P_CSV = 'D:\\GIV\\givtrans_api_automation\\Response_File\\QTA.csv'
QTA_A_CSV = 'D:\\GIV\\givtrans_api_automation\\Response_File\\QTA.csv'
QIA_CSV = 'D:\\GIV\\givtrans_api_automation\\Response_File\\QIA.csv'

