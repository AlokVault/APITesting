""" Convert Channel CSV to Json """
import json
from datetime import datetime, timedelta
import pandas as pd

from csv_json_names import USERNAME, TARGET_NAME_SCRIPT, CHANNEL_APINAME, PASSWORD, \
    WMS_APINAME, CAMPAIGN_APINAME, CHANNEL_TRANSACTION_CSV, JSONNAME_FOR_CHANNEL_TRANSACTION, \
    SCRIPTFILE_TRANSACTION, TRANSACTION_CSV_LIST

"""If in CSV any value is inserted in the commented colummn , un-comment that feild and provide
    the varialble in if loop """


def all_transaction_json():
    """ Transaction CSV to Json"""
    list_index = 0
    read = 'A'
    for _ in range(len(TRANSACTION_CSV_LIST)):

        _df = pd.read_excel(CHANNEL_TRANSACTION_CSV + "\\" + TRANSACTION_CSV_LIST[list_index])
        get_in_csv = _df._values
        date_time_stamp = datetime.utcnow().isoformat()
        local_date = datetime.utcnow().date()
        current_date_time_stamp = datetime.utcnow().isoformat()
        ship_date = local_date + timedelta(1)
        shipment__date = str(ship_date)
        updated_local_date = str(local_date)
        future_end_date = local_date + timedelta(4)
        campaign_future_end_date = str(future_end_date)

        ''' channel Transaction '''
        if "shipDate" in _df.columns:
            if list_index == 13:
                _df = _df[
                    [
                        "transactionNumber",
                        "channel",
                        # "campaignCode",
                        "dateTimeStamp",
                        "user",
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
                        "salesOrderNumber",
                        "orderType",
                        "shipDate",
                        "inventorySource",
                        "qty",
                        "action"
                    ]]

                df1 = _df.groupby(
                    [
                        "transactionNumber",
                        "channel",
                        # "campaignCode",
                        "dateTimeStamp",
                        "user",
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
                        "salesOrderNumber",
                        "orderType",
                        "shipDate",
                        "inventorySource",
                        "qty",
                        "action"]).sum()
                df1 = df1.reset_index()

                #     # print(df1)
                _d = dict()
                for header in df1.values:
                    transaction_number = header[0]
                    channel = header[1]
                    campaign_code = header[2]
                    date_time_stamp = current_date_time_stamp
                    user = "givadmin"

                _d = {"transactionNumber": transaction_number, "channel": channel,
                      "campaignCode": "",
                      "dateTimeStamp": date_time_stamp, "user": user, "multipleSkus": []}
            else:
                _df = _df[
                    [
                        "transactionNumber",
                        "channel",
                        "campaignCode",
                        "dateTimeStamp",
                        "user",
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
                        "salesOrderNumber",
                        "orderType",
                        "shipDate",
                        "inventorySource",
                        "qty",
                        "action"
                    ]]

                df1 = _df.groupby(
                    [
                        "transactionNumber",
                        "channel",
                        "campaignCode",
                        "dateTimeStamp",
                        "user",
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
                        "salesOrderNumber",
                        "orderType",
                        "shipDate",
                        "inventorySource",
                        "qty",
                        "action"]).sum()
                df1 = df1.reset_index()

                #     # print(df1)
                _d = dict()
                for header in df1.values:
                    transaction_number = header[0]
                    channel = header[1]
                    campaign_code = header[2]
                    date_time_stamp = current_date_time_stamp
                    user = "givadmin"

                _d = {"transactionNumber": transaction_number, "channel": channel,
                      "campaignCode": campaign_code,
                      "dateTimeStamp": date_time_stamp, "user": user, "multipleSkus": []}

            # count = 0
            for line in get_in_csv:
                # company = line[5]
                # division = line[6]
                # warehouse = line[7]
                # manufacturing_plant_code = line[8]
                sku_barcode = line[8]
                # season = line[9]
                # season_year = line[10]
                style = line[11]
                style_sfx = line[12]
                color = line[13]
                # color_sfx = line[14]
                # sec_dimension = line[15]
                quality = line[16]
                size_rnge_code = line[17]
                size_rel_posn_in = line[18]
                inventory_type = line[19]
                # lotNumber = line[20]
                # country_of_origin = line[21]
                product_status = line[22]
                # sku_attribute1 = line[23]
                # sku_attribute2 = line[24]
                # sku_attribute3 = line[25]
                # sku_attribute4 = line[26]
                # sku_attribute5 = line[27]
                sales_order_number = line[28]
                order_type = line[29]
                ship_date = shipment__date
                inventory_source = line[31]
                qty = line[32]
                action = line[33]

                category_list = []
                for item in _d['multipleSkus']:
                    category_list.append(item['company'])

                if not transaction_number in category_list:
                    _d['multipleSkus'].append(
                        {
                            "company": "",
                            "division": "",
                            "warehouse": "",
                            "manufacturingPlantCode": "",
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
                            "salesOrderNumber": sales_order_number,
                            "orderType": order_type,
                            "shipDate": ship_date,
                            "inventorySource": inventory_source,
                            "qty": qty,
                            "action": action
                        })

            with open(JSONNAME_FOR_CHANNEL_TRANSACTION + read + ".json", "w") as _f:
                _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))
                scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -_d "@' + \
                                   JSONNAME_FOR_CHANNEL_TRANSACTION + "_" + read + ".json" + \
                                   '" -X POST -H "Content-Type: application/json" http://' + \
                                   TARGET_NAME_SCRIPT + ':8080/api/' + CHANNEL_APINAME + '\n'
                SCRIPTFILE_TRANSACTION.write(scriptfileoutput)
                list_index += 1
                _x = ord(read) + 1
                _y = chr(_x)
                read = _y
                _f.close()

        elif "serialNumber" in _df.columns:
            get_in_csv = _df._values
            _df = _df[["transactionNumber",
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

            df1 = _df.groupby(
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
            df1 = df1.reset_index()
            #
            #     # print(df1)
            _d = dict()
            for header in df1.values:
                transaction_number = header[0]
                date_time_stamp = current_date_time_stamp
                user = header[2]
            _d = {"transactionNumber": transaction_number, "dateTimeStamp": date_time_stamp,
                  "user": user,
                  "multipleSkus": []}

            for line in get_in_csv:
                # company = line[3]
                # division = line[4]
                warehouse = line[5]
                sku_barcode = line[6]
                # season = line[7]
                # seasonYear = line[8]
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

                category_list = []
                for item in _d['multipleSkus']:
                    category_list.append(item['company'])

                if not transaction_number in category_list:
                    # _d['dateTimeStamp'].append(dateTimeStamp)
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

            with open(JSONNAME_FOR_CHANNEL_TRANSACTION + read + ".json", "w") as _f:
                _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))
                scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -_d "@' + \
                                   JSONNAME_FOR_CHANNEL_TRANSACTION + "_" + read + ".json" + \
                                   '" -X POST -H "Content-Type: application/json" http://' + \
                                   TARGET_NAME_SCRIPT + ':8080/api/' + WMS_APINAME + '\n'
                SCRIPTFILE_TRANSACTION.write(scriptfileoutput)
                list_index += 1
                _x = ord(read) + 1
                _y = chr(_x)
                read = _y
                _f.close()


        elif "campaignStartDate" in _df.columns:
            get_in_csv = _df._values
            _df = _df[[
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
                "minQty",
                "maxQty",
                "protectQty",
                "autoReplenish"
            ]]

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
                campaign_start_date = updated_local_date
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

            with open(JSONNAME_FOR_CHANNEL_TRANSACTION + read + ".json", "w") as _f:
                _f.write(json.dumps(_d, sort_keys=False, indent=4, separators=(',', ': ')))
                scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -_d "@' + \
                                   JSONNAME_FOR_CHANNEL_TRANSACTION + "_" + read + ".json" + \
                                   '" -X POST -H "Content-Type: application/json" http://' + \
                                   TARGET_NAME_SCRIPT + ':8080/api/' + CAMPAIGN_APINAME + '\n'
                SCRIPTFILE_TRANSACTION.write(scriptfileoutput)
                list_index += 1
                _x = ord(read) + 1
                _y = chr(_x)
                read = _y
                _f.close()
all_transaction_json()
