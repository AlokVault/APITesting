''' Query Response Save'''
import csv
import json

from csv_json_names import QTA_P_CSV, QTA_A_CSV, QIA_CSV

class QueryResponseToCsv:
    ''' Class for Query Response Saving '''
    def qta_query_protect(self, qta_response_protect):
        ''' QTA Query Save Response'''
        text = json.loads(qta_response_protect)
        with open(QTA_P_CSV, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["transactions"]
            csvwriter.writerow(["company", "division", "warehouse", "skuBarcode",
                                "protectedQuantity", "campaignCode", "channel", "reasonCode"])
            for _l in line:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"],
                                    _l["protectedQuantity"], _l["campaignCode"], _l["channel"],
                                    _l["reasonCode"]])


        csv_file.close()
    def qta_query_allocate(self, qta_response_allocate):
        """Qta Query Save Response"""
        text1 = json.loads(qta_response_allocate)
        with open(QTA_A_CSV, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line1 = text1["transactions"]
            csvwriter.writerow(["company", "division", "warehouse", "skuBarcode",
                                "allocatedQuantity", "campaignCode", "channel", "reasonCode"])
            for _l in line1:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"],
                                    _l["allocatedQuantity"], _l["campaignCode"], _l["channel"],
                                    _l["reasonCode"]])


        csv_file.close()

    def qia_query(self, qia_response_result1):
        ''' QIA Query response save'''
        text = json.loads(qia_response_result1)
        with open(QIA_CSV, 'a') as csv_file:
            csvwriter = csv.writer(csv_file, delimiter=',')
            line = text["skus"]
            csvwriter.writerow(["company", "division", "warehouse", "skuBarcode",
                                "allocatedQty", "protectedQty", "onHandQty", "availableQty",
                                "lockedQty",])
            for _l in line:
                csvwriter.writerow([_l["company"], _l["division"], _l["warehouse"],
                                    _l["skuBarcode"], _l["allocatedQty"], _l["protectedQty"],
                                    _l["onHandQty"], _l["availableQty"], _l["lockedQty"]])

        csv_file.close()
