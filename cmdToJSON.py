from datetime import datetime
import json
import csv


def saveAsJSON(cmd_out, outputFileName):
    try:
        json_data = {}
        reader = csv.DictReader(cmd_out.splitlines())
        #print(contents)
        json_data["contents"] = list(reader)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        #print(current_time)
        json_data["timestamp"] = current_time

        output_file = outputFileName + ".json"
        with open(output_file, "w") as outfile:
            data = json.dump(json_data, outfile, indent=4, separators=(',', ': '))

    except Exception as e:
        raise e

if __name__ == '__main__':
    #saveAsJSON("./output_test", "result")
    print("Used for testing")
