''' Item Save response '''
import csv
import json
import os
from csv_json_names import ITEM_RESPONSE_FILE

class ItemResponseCsv1:
    ''' Class for Saving Item Response '''
    def item_response_sent_to_csv1(self, item_response_result):
        ''' function for saving response '''
        text = json.loads(item_response_result)
        if os.path.isfile(ITEM_RESPONSE_FILE):
            is_header = True
        else:
            is_header = False

        with open(ITEM_RESPONSE_FILE, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["content"]
            if not is_header:
                csvwriter.writerow(["company", "division", "warehouse", "skuBarcode"])
            for _l in line:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"]])

        csv_file.close()
