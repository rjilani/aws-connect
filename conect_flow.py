from utils.fileutil import read_json_file
from utils.fileutil import dateconverter
import json

if __name__ == '__main__':
    # list_instances()
    # list_queues()
    # list_phones()
    # create_instances()
    data = read_json_file("data/Inbound Flow.json")

    print(type(data))

    # for i in data:
    #     print(i)

    json_string = json_string = json.dumps(data, sort_keys=True, indent=4, default=dateconverter)
    print(json_string)