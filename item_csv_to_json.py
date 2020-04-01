''' Logic for converting CSV to Json'''
import csv
import json
from datetime import datetime

from csv_json_names import SCRIPTNAME_FOR_ITEM, CSV_FOR_ITEM, JSONNAME_FOR_ITEM
from csv_json_names import USERNAME, PASSWORD, TARGET_NAME_SCRIPT, ITEM_APINAME

DATE_TIME_STAMP = datetime.utcnow().isoformat()
CSVFILE = open(CSV_FOR_ITEM, 'r', encoding='latin-1')
SCRIPTFILE = open(SCRIPTNAME_FOR_ITEM, 'w')
READER = csv.DictReader(CSVFILE)


def item_json():
    '''Function for converting CSV to JSon '''
    recordcount = 0
    def update_json_file():
        json_file1 = open(jfilename, "r")  # Open the JSON file for reading
        data = json.load(json_file1)  # Read the JSON into the buffer
        json_file1.close()  # Close the JSON file

        ## Working with buffered content
        data["dateTimeStamp"] = DATE_TIME_STAMP

        ## Save our changes to JSON file
        json_file2 = open(jfilename, "w+")
        json_file2.write(json.dumps(data, indent=4))
        json_file2.close()

    for row in READER:
        jfilename = JSONNAME_FOR_ITEM + "_" + str(recordcount) + ".json"
        json_file = open(jfilename, "w")
        out = json.dumps(row)
        json_file.write(out)
        json_file.close()
        scriptfileoutput = 'curl -u ' + USERNAME + ':' + PASSWORD + ' -d "@' + jfilename +\
                           '" -X POST -H "Content-Type: application/json" http://' + \
                           TARGET_NAME_SCRIPT + ':8080/api/' + ITEM_APINAME + '\n'
        SCRIPTFILE.write(scriptfileoutput)
        recordcount += 1
        update_json_file()


item_json()
