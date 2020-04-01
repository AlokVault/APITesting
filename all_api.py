''' All Api's call request '''
from datetime import datetime
import pyfiglet

from item_csv_to_json import item_json
from wms_request import wms_json
from campaign_create import campaigncreatejson
# from campaign_data_update import campaign_data_update_json
# from campaign_header_update import campaign_header_update_json
# from transaction import all_transaction_json
# # #
from send_request import item_post
# from send_request import item_get
from send_request import wms_post
from send_request import campaign_create
# from send_request import campaign_update
# from send_request import transaction_post

TIME_IST = datetime.now().time()
TIME = str(TIME_IST)
if TIME > "12" and TIME < "16":
    ASCII_BANNER = pyfiglet.figlet_format("Good Afternoon \n                 GIV AUTOMATION BY -    ALOK")
    print(ASCII_BANNER)

elif TIME < "12":
    ASCII_BANNER = pyfiglet.figlet_format("Good Morning \n                  GIV AUTOMATION BY -      ALOK")
    print(ASCII_BANNER)
else:
    ASCII_BANNER = pyfiglet.figlet_format("Good Evening \n                  GIV AUTOMATION BY -      ALOK")
    print(ASCII_BANNER)

""" CSV TO JSON """
item_json()
print("*********Item CSV Converted in Json********* \n \n")

wms_json()
print("*********Wms CSV converted to Json**********\n \n")

campaigncreatejson()
print("*********CampaignCreate CSV convrted to Json*********\n \n")
#
# campaign_data_update_json()
# print("*********Campaign Data Update CSV convrted to Json*********\n \n")
# #
# campaign_header_update_json()
# print("*********Campaign header Update CSV convrted to Json*********\n \n")
#
# all_transaction_json()
# print("*************** All Transction CSV converted to Json *****************\n \n")

# '''APi Request'''
item_post()
# item_get()
wms_post()
campaign_create()
# campaign_update()
# transaction_post()
