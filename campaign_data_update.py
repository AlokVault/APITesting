""" CSV For Campaign with data  is converted into Json"""
import json
from datetime import datetime, timedelta
import pandas as pd
from csv_json_names import JSONNAME_FOR_CAMPAIGN_DETAIL_UPDATE, \
    CSV_FOR_CAMPAIGN_DETAIL_UPDATE, USERNAME, PASSWORD, TARGET_NAME_SCRIPT, CAMPAIGN_APINAME, \
    SCRIPTNAME_FOR_CAMPAIGN_DETAIL_UPDATE


def campaign_data_update_json():
    """ Convert CSV TO Json """
    script_file = open(SCRIPTNAME_FOR_CAMPAIGN_DETAIL_UPDATE, "w")
    _df = pd.read_excel(CSV_FOR_CAMPAIGN_DETAIL_UPDATE)
    get_in_csv = _df._values
    # scriptfile = open(scriptname_for_campaign_create, 'w')

    # Get the local time and future time
    local_date = datetime.utcnow().date()
    updated_local_date = str(local_date)
    date_time_stamp = datetime.utcnow().isoformat()
    future_end_date = local_date + timedelta(4)

    # Change the dates into str form
    campaign_future_end_date = str(future_end_date)
    # choose columns to keep, in the desired nested json hierarchical order
    _df = _df[["transactionNumber",
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
               ]]

    # order in the groupby here matters, it determines the json nesting
    # the groupby call makes a pandas series by grouping "category",
    # "sub_category" and"sub_category_type",
    # while summing the numerical column 'count'
    _df1 = _df.groupby(
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
         ]).sum()
    _df1 = _df1.reset_index()

    # print(df1)
    _d = dict()
    for header in _df1.values:
        transaction_number = header[0]
        channel = header[1]
        campaign_code = header[2]
        campaign_start_date = updated_local_date
        campaign_end_date = campaign_future_end_date
        campaign_active = header[5]
        action = header[6]
        user = header[7]
        date_time_stamp = date_time_stamp
    _d = {"transactionNumber": transaction_number, "channel": channel,
          "campaignCode": campaign_code,
          "campaignStartDate": campaign_start_date,
          "campaignEndDate": campaign_end_date, "campaignActive": campaign_active, "action": action,
          "user": user,
          "dateTimeStamp": date_time_stamp, "campaignDetails": []}
    for line in get_in_csv:
        # company = line[9]
        # division = line[10]
        # warehouse = line[11]
        sku_barcode = line[12]
        # season = line[13]
        # season_year = line[14]
        style = line[15]
        style_sfx = line[16]
        color = line[17]
        # color_sfx = line[18]
        # sec_dimension = line[19]
        quality = line[20]
        size_rnge_code = line[21]
        size_rel_posn_in = line[22]
        inventory_type = line[23]
        # lot_number = line[24]
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
        # print("mmknkjn=",category_list)
        # if 'category' is NOT category_list, append it
        if not transaction_number in category_list:
            # d['dateTimeStamp'].append(dateTimeStamp)
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

    with open(JSONNAME_FOR_CAMPAIGN_DETAIL_UPDATE, "w") as _f:
        _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))  # for pretty
        scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -d "@' + \
        JSONNAME_FOR_CAMPAIGN_DETAIL_UPDATE + \
        '" -X POST -H "Content-Type: application/json" http://' + TARGET_NAME_SCRIPT + ':8080/api/'\
                           + CAMPAIGN_APINAME + '\n'
        script_file.write(scriptfileoutput)
        _f.close()


campaign_data_update_json()
