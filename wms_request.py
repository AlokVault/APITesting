''' WMS Request '''
import json
from datetime import datetime
import pandas as pd
from csv_json_names import CSV_FOR_WMS, JSONNAME_FOR_WMS, \
    SCRIPTNAME_FOR_WMS, WMS_APINAME, \
    TARGET_NAME_SCRIPT, USERNAME, PASSWORD

def wms_json():
    """ WMS Logic """
    recordcount = 1
    _df = pd.read_excel(CSV_FOR_WMS)
    get_in_csv = _df._values

    scriptfile = open(SCRIPTNAME_FOR_WMS, 'w')

    # Get the local time and future time

    current_date_time_stamp = datetime.utcnow().isoformat()

    # choose columns to keep, in the desired nested json hierarchical order
    _df = _df[[
        "transactionNumber",
        "dateTimeStamp",
        "user",
        # "company",
        # "division",
        "warehouse",
        "skuBarcode",
        # "season",
        # "seasonYear",
        "style",
        "styleSfx",
        "color",
        # "colorSfx",
        # "secDimension",
        "quality",
        "sizeRngeCode",
        "sizeRelPosnIn",
        "inventoryType",
        # "lotNumber",
        # "countryOfOrigin",
        "productStatus",
        # "skuAttribute1",
        # "skuAttribute2",
        # "skuAttribute3",
        # "skuAttribute4",
        # "skuAttribute5",
        # "serialNumber",
        "qty",
        "action",
        "inventorySource",
        "reasonCode",
        # "desc"
    ]]

    # order in the groupby here matters, it determines the json nesting
    # the groupby call makes a pandas series by grouping "category",
    # "sub_category" and"sub_category_type",
    # while summing the numerical column 'count'
    _df1 = _df.groupby(
        [
            "transactionNumber",
            "dateTimeStamp",
            "user",
            # "company",
            # "division",
            "warehouse",
            "skuBarcode",
            # "season",
            # "seasonYear",
            "style",
            "styleSfx",
            "color",
            # "colorSfx",
            # "secDimension",
            "quality",
            "sizeRngeCode",
            "sizeRelPosnIn",
            "inventoryType",
            # "lotNumber",
            # "countryOfOrigin",
            "productStatus",
            # "skuAttribute1",
            # "skuAttribute2",
            # "skuAttribute3",
            # "skuAttribute4",
            # "skuAttribute5",
            # "serialNumber",
            "qty",
            "action",
            "inventorySource",
            "reasonCode",
            # "desc"
        ]).sum()
    _df1 = _df1.reset_index()

    # print(df1)
    _d = dict()
    for header in _df1.values:
        transaction_number = header[0]
        date_time_stamp = current_date_time_stamp
        user = header[2]
    _d = {"transactionNumber": transaction_number, "dateTimeStamp": date_time_stamp,
          "user": user, "multipleSkus": []}

    count = 0
    for line in get_in_csv:
        # company = line[3]
        # division = line[4]
        warehouse = line[5]
        sku_barcode = line[6]
        # season = line[7]
        # season_year = line[8]
        style = line[9]
        style_sfx = line[10]
        color = line[11]
        # color_sfx = line[12]
        # sec_dimension = line[13]
        quality = line[14]
        size_rnge_code = line[15]
        size_rel_posn_in = line[16]
        inventory_type = line[17]
        # lot_number = line[18]
        # country_of_origin = line[19]
        product_status = line[20]
        # sku_attribute1 = line[21]
        # sku_attribute2 = line[22]
        # sku_attribute3 = line[23]
        # sku_attribute4 = line[24]
        # sku_attribute5 = line[25]
        # serial_number = line[26]
        qty = line[27]
        action = line[28]
        inventory_source = line[29]
        # reason_code = line[30]
        # desc = line[31]

        # make a list of keys
        category_list = []
        for item in _d['multipleSkus']:
            category_list.append(item['company'])
        # print("mmknkjn=",category_list)
        # if 'category' is NOT category_list, append it
        if not transaction_number in category_list:
            # d['dateTimeStamp'].append(dateTimeStamp)
            _d['multipleSkus'].append(
                {
                    "company": "",
                    "division": "",
                    "warehouse": warehouse,
                    "skuBarcode": sku_barcode,
                    "season": "",
                    "seasonYear": "",
                    "style": style,
                    "styleSfx": style_sfx,
                    "color": color,
                    "colorSfx": "",
                    "secDimension": "",
                    "quality": quality,
                    "sizeRngeCode": size_rnge_code,
                    "sizeRelPosnIn": size_rel_posn_in,
                    "inventoryType": inventory_type,
                    "lotNumber": "",
                    "countryOfOrigin": "",
                    "productStatus": product_status,
                    "skuAttribute1": "",
                    "skuAttribute2": "",
                    "skuAttribute3": "",
                    "skuAttribute4": "",
                    "skuAttribute5": "",
                    "serialNumber": "",
                    "qty": qty,
                    "action": action,
                    "inventorySource": inventory_source,
                    "reasonCode": "",
                    "desc": ""
                })

            count += 1

    with open(JSONNAME_FOR_WMS, "w") as _f:
        _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))  # for pretty
        scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -d "@' + \
                           JSONNAME_FOR_WMS + '" -X POST -H "Content-Type: application/json" ' \
                                              'http://' + TARGET_NAME_SCRIPT + ':8080/api/' + \
                           WMS_APINAME + '\n'
        scriptfile.write(scriptfileoutput)
        recordcount += 1
        scriptfile.close()


wms_json()
