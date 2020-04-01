''' Campaign CSV to Json '''
import csv
import json
import os
from csv_json_names import CAMPAIGN_RESPONSE_FILE

class CampaignCreateResponseToCsv:
    ''' Class for CSV to Json '''
    def campaign_response_csv(self, campaign_result):
        """ Logic for CSV to Json """
        text = json.loads(campaign_result)
        if os.path.isfile(CAMPAIGN_RESPONSE_FILE):
            is_header = True
        else:
            is_header = False

        with open(CAMPAIGN_RESPONSE_FILE, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["campaignDetails"]
            if not is_header:
                csvwriter.writerow(
                    ["company", "division", "warehouse", "skuBarcode", "minQty", "maxQty",
                     "protectQty",
                     "autoReplenish", "channel", "campaignCode", "campaignStartDate",
                     "campaignEndDate", "campaignActive", "action", "responseDetail"])
            for _l in line:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"], _l["minQty"], _l["maxQty"], _l["protectQty"],
                                    _l["autoReplenish"], _l["channel"], _l["campaignCode"],
                                    _l["campaignStartDate"], _l["campaignEndDate"],
                                    _l["campaignActive"], _l["action"], _l["responseDetail"]])
        csv_file.close()
