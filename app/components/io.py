import requests
import numpy
import time
import datetime
import os
import json
import csv
import xmltodict

headers = {"Content-Type":"application/json",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0", 
"Connection": "close"}

XMLheaders = {"Content-Type":"application/xml",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0", 
"Connection": "close"}


def convert_XML2JSON(res):
    # print(res.content)
    xmltodict_data = xmltodict.parse(res)
    print(type(xmltodict_data))

    json_data= json.dumps(xmltodict_data, ensure_ascii=False, indent=4, sort_keys=True)
    #print(json_data)
    x= open("../data/RL_S.json","w")
    x.write(json_data)
    x.close()


def requests_from_url(url, fileType="json"):
    if fileType.upper() == "XML":
        try:
            print(url)
            res = requests.get(url, headers=XMLheaders)
            print(res.status_code)
            print(res)

            #write xml file into the HDD
            myfile = open("../data/RL_S.xml", "w")
            myfile.write(res.text)

            return res

            
        except:
            print("cannot get the files")
        finally:
            print("finish the url request action")
    else:
        try:
            print("url: {}".format(url))
            res = requests.get(url, headers)
            if res.status_code == 200:
                return res.json()
            else:
                return ""
        except:
            return ""
        finally:
            print("finish the url request action")

def write_file(path, fileName, dataToWrite, JSONFORMAT=True):
    """
    JSONFORMAT (bool): default is true if not passing in, if value passing in is false, meaning the file to write is CSV
    """

    if JSONFORMAT:
        with open(path + fileName, 'w', encoding='utf-8') as f:
            json.dump(dataToWrite, f, ensure_ascii=False, indent=4)
    else:
        #it will write CSV file
        print("it will write CSV file")

        with open(path + fileName, 'w', newline='') as csvfile:
            fieldnames = ['first_name', 'last_name']
            writer = csv.DictWriter(csvfile, fieldnames=dataToWrite[0])

            writer.writeheader()

            writer.writerows(dataToWrite[1])
        