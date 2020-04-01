''' Channel Save response'''
import csv
import json
import os
from csv_json_names import CHANNEL_RESPONSE_FILE

class ChannelResponseToCsv:
    '''' Class for channel save response '''
    def channel_response_csv(self, channel_response_result):
        '''' Channel Save response '''
        text = json.loads(channel_response_result)
        if os.path.isfile(CHANNEL_RESPONSE_FILE):
            is_header = False
        else:
            is_header = True
        with open(CHANNEL_RESPONSE_FILE, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["multipleSkus"]
            if  is_header == True:
                csvwriter.writerow(["channel", "campaignCode", "company", "division", "warehouse",
                                    "skuBarcode", "shipDate", "inventorySource", "requestedQty",
                                    "responseQty", "onHandQty", "protectedQty", "allocatedQty",
                                    "lockedQty", "availableQty", "action", "responseDetail"])
            for _l in line:
                csvwriter.writerow([_l["channel"], _l["campaignCode"], _l["company"],
                                    _l["division"], _l["warehouse"], _l["skuBarcode"],
                                    _l["inventorySource"], _l["requestedQty"], _l["responseQty"],
                                    _l["onHandQty"], _l["protectedQty"], _l["allocatedQty"],
                                    _l["lockedQty"], _l["availableQty"], _l["action"],
                                    _l["responseDetail"]])

        csv_file.close()
