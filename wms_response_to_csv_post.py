'''' WMS response Saving '''
import csv
import json
import os
from csv_json_names import WMS_RESPONSE_FILE

class WmsResponseToCsv:
    ''' Class for Wms Save '''
    def response_csv(self, result):
        ''' Function for Wms Response Save'''
        text = json.loads(result)

        if os.path.isfile(WMS_RESPONSE_FILE):
            is_header = True
        else:
            is_header = False
        with open(WMS_RESPONSE_FILE, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["multipleSkus"]
            if not is_header:
                csvwriter.writerow(["company", "division", "warehouse", "skuBarcode",
                                    "requestedQty", "responseQty", "onhandQty", "allocatedQty",
                                    "protectedQty", "lockedQty", "availableQty", "action",
                                    "inventorySource", "reasonCode", "desc", "responseDetail"])
            for _l in line:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"],
                                    _l["requestedQty"], _l["responseQty"], _l["onhandQty"],
                                    _l["allocatedQty"], _l["protectedQty"], _l["lockedQty"],
                                    _l["availableQty"], _l["action"], _l["inventorySource"],
                                    _l["reasonCode"], _l["desc"], _l["responseDetail"]])
        csv_file.close()
