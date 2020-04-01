''' Convert CSV for campaign header update to json '''
import csv
import json
from datetime import datetime, timedelta
from csv_json_names import CSV_FOR_CAMPAIGN_HEADER_UPDATE, \
    SCRIPTNAME_FOR_CAMPAIGN_HEADER_UPDATE, JSONNAME_FOR_CAMPAIGN_HEADER_UPDATE,\
    USERNAME, PASSWORD, TARGET_NAME_SCRIPT, \
    CAMPAIGN_APINAME

CSV_FILE = open(CSV_FOR_CAMPAIGN_HEADER_UPDATE, 'r', encoding='latin-1')
SCRIPT_FILE = open(SCRIPTNAME_FOR_CAMPAIGN_HEADER_UPDATE, 'w')
READER = csv.DictReader(CSV_FILE)


def campaign_header_update_json():
    ''' Function for CSV to Json'''
    # current = datetime.utcnow().isoformat()
    date_time_stamp = datetime.utcnow().isoformat()

    # Get the local time and future time
    local_date = datetime.utcnow().date()
    updated_local_date = str(local_date)
    start_date = updated_local_date
    future_end_date = local_date + timedelta(4)
    #
    #     #Change the dates into str form
    campaign_future_end_date = str(future_end_date)
    recordcount = 4

    def update_json_file():
        json_file1 = open(jfilename, "r")  # Open the JSON file for reading
        data = json.load(json_file1)  # Read the JSON into the buffer
        json_file1.close()  # Close the JSON file

        ## Working with buffered content
        data["dateTimeStamp"] = date_time_stamp
        data["campaignStartDate"] = start_date
        data["campaignEndDate"] = campaign_future_end_date

        ## Save our changes to JSON file
        json_file2 = open(jfilename, "w+")
        json_file2.write(json.dumps(data, indent=2))
        json_file2.close()

    for row in READER:
        jfilename = JSONNAME_FOR_CAMPAIGN_HEADER_UPDATE + "_0" + str(recordcount) + ".json"
        jsonfile = open(jfilename, "w")
        out = json.dumps(row, indent=4)
        jsonfile.write(out)
        jsonfile.close()
        scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -d "@' + jfilename+\
                           '" -X POST -H "Content-Type: application/json" http://' +\
                           TARGET_NAME_SCRIPT + ':8080/api/' + CAMPAIGN_APINAME + '\n'
        SCRIPT_FILE.write(scriptfileoutput)
        recordcount += 1
        update_json_file()


campaign_header_update_json()
