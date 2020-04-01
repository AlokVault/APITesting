''' Creates Campaign Json'''

import json
from datetime import datetime, timedelta
import pandas as pd
from csv_json_names import CSV_FOR_CAMPAIGN_CREATE, \
    JSONNAME_FOR_CAMPAIGN_CREATE, CAMPAIGN_CREATE_LIST, USERNAME, PASSWORD,\
    SCRIPTNAME_FOR_CAMPAIGN_CREATE, \
    TARGET_NAME_SCRIPT, CAMPAIGN_APINAME


# scriptname_for_campaign_create

def campaigncreatejson():
    ''' CSV to Json Convert '''
    list_index = 0
    script_file = open(SCRIPTNAME_FOR_CAMPAIGN_CREATE, "w")

    for _ in range(len(CAMPAIGN_CREATE_LIST)):
        _df = pd.read_excel(CSV_FOR_CAMPAIGN_CREATE + "\\" + CAMPAIGN_CREATE_LIST[list_index])
        get_in_csv = _df._values
        # scriptfile = open(scriptname_for_campaign_create, 'w')

        # Get the local time and future time
        local_date = datetime.utcnow().date()
        date_time_stamp = datetime.utcnow().isoformat()
        future_start_date = local_date + timedelta(1)
        future_end_date = local_date + timedelta(4)

        # Change the dates into str form
        campaign_future_start_date = str(future_start_date)
        campaign_future_end_date = str(future_end_date)
        # choose columns to keep, in the desired nested json hierarchical order
        _df = _df[
            ["transactionNumber",
             "channel",
             "campaignCode",
             "campaignStartDate",
             "campaignEndDate",
             "campaignActive",
             "action",
             "user",
             "dateTimeStamp",
             # "company",
             # "division",
             # "warehouse",
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
             "minQty",
             "maxQty",
             "protectQty",
             "autoReplenish"
             ]
        ]

        # order in the groupby here matters, it determines the json nesting
        # the groupby call makes a pandas series by grouping "category",
        # "sub_category" and"sub_category_type",
        # while summing the numerical column 'count'
        df1 = _df.groupby([
            "transactionNumber",
            "channel",
            "campaignCode",
            "campaignStartDate",
            "campaignEndDate",
            "campaignActive",
            "action",
            "user",
            "dateTimeStamp",
            # "company",
            # "division",
            # "warehouse",
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
            # "minQty",
            # "maxQty",
            # "protectQty",
            # "autoReplenish"
        ]).sum()
        df1 = df1.reset_index()

        # print(df1)
        _d = dict()
        for header in df1.values:
            transaction_number = header[0]
            channel = header[1]
            campaign_code = header[2]
            campaign_start_date = campaign_future_start_date
            campaign_end_date = campaign_future_end_date
            campaign_active = header[5]
            action = header[6]
            user = header[7]
            date_time_stamp = date_time_stamp
        _d = {"transactionNumber": transaction_number, "channel": channel,
              "campaignCode": campaign_code, "campaignStartDate": campaign_start_date,
              "campaignEndDate": campaign_end_date, "campaignActive": campaign_active,
              "action": action, "user": user, "dateTimeStamp": date_time_stamp,
              "campaignDetails": []}
        for line in get_in_csv:
            # company = line[9]
            # division = line[10]
            # warehouse = line[11]
            sku_barcode = line[12]
            # season = line[13]
            # seasonYear = line[14]
            style = line[15]
            style_sfx = line[16]
            color = line[17]
            # colorSfx = line[18]
            # secDimension = line[19]
            quality = line[20]
            size_rnge_code = line[21]
            size_rel_posn_in = line[22]
            inventory_type = line[23]
            # lotNumber = line[24]
            # countryOfOrigin = line[25]
            product_status = line[26]
            # skuAttribute1 = line[27]
            # skuAttribute2 = line[28]
            # skuAttribute3 = line[29]
            # skuAttribute4 = line[30]
            # skuAttribute5 = line[31]
            min_qty = line[32]
            max_qty = line[33]
            protect_qty = line[34]
            auto_replenish = line[35]

            # make a list of keys
            category_list = []

            for item in _d['campaignDetails']:
                category_list.append(item['company'])
            # if 'category' is NOT category_list, append it
            if not transaction_number in category_list:
                _d['campaignDetails'].append(
                    {
                        "company": "",
                        "division": "",
                        "warehouse": "",
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
                        "minQty": min_qty,
                        "maxQty": max_qty,
                        "protectQty": protect_qty,
                        "autoReplenish": auto_replenish
                    })


        #
        with open(JSONNAME_FOR_CAMPAIGN_CREATE + "_0" + str(list_index) + ".json", "w") as _f:
            _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))
            scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -d "@' +\
                               JSONNAME_FOR_CAMPAIGN_CREATE + "_0" + str(list_index) +\
                               ".json" + '" -X POST -H "Content-Type: application/json" http://' +\
                               TARGET_NAME_SCRIPT + ':8080/api/' + CAMPAIGN_APINAME + '\n'
            script_file.write(scriptfileoutput)
            list_index += 1
            _f.close()


campaigncreatejson()
