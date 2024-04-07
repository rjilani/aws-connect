import json
import datetime


def dateconverter(o):
    if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
        return o.__str__()


def write_json_file(filelocation, text):
    try:
        with open(filelocation, 'w', encoding='utf-8') as f:
            f.write(text)
    except Exception as ex:
        print(str(ex))


def read_json_file(filelocation):
    try:
        with open(filelocation) as f:
            data = json.load(f)
            return data
    except Exception as ex:
        print(str(ex))
