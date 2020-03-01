import os
import argparse
from pathlib import Path
from dotenv import load_dotenv
import pymongo
import pysrt
import re
import time
import json

env_dir = Path(os.path.dirname(__file__)).parent
env_path = os.path.join(env_dir, '.env')
load_dotenv(dotenv_path=env_path)

def srt_to_json(filename):
    subs = pysrt.open(filename)

    data = {}
    temp = []

    for sub in subs:
        text = sub.text
        try:
            # print(sub.index)
            reg_exp = re.findall(r'GPRMC,(.*)',text)[0].split(',')
            latitude = str(round(int(reg_exp[2][:-8]) +float(reg_exp[2][-8:])/60, 6)) + ' ' + reg_exp[3]
            longitude = str(round(int(reg_exp[4][:-8]) + float(reg_exp[4][-8:])/60, 6)) + ' ' + reg_exp[5]
            str_time = time.strptime(reg_exp[0][:6] + reg_exp[8] + 'UTC', '%H%M%S%d%m%y%Z')
            temp.append({
                'index': sub.index,
                'latitude': latitude,
                'longitude': longitude,
                'datetime': str(str_time)       
            })
            # print(temp)
        except IndexError as e:
            # print(e)
            pass

    data[filename] = temp

    return data

    # client = pymongo.MongoClient(os.getenv('MLAB_URI'), retryWrites = False)
    # db = client.get_default_database()
    # signs = db.signs
    # signs.insert_many(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert MP4s into JPGs')
    parser.add_argument('-i', '--input_file', type=str, required=True, help='MP4 filepath')
    args = parser.parse_args()

    json = srt_to_json(args.input_file)
    print(json)