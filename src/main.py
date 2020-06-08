from unicodedata import normalize
import docx2txt
import re
import json
import pandas as pd
from os import listdir
from schema import schemas


DEBUG = False


def main():
    print("DOCX-19")

    docsJson = []
    fileList = listdir("assets")

    print("Read {} Docs ".format(len(fileList)))
    for fileName in fileList:
        print(".", end="")

        text = docx2txt.process('assets/{}'.format(fileName))
        text = text.lower()
        text = removeAcentos(text)

        if(DEBUG):
            fileTxt = open("output-temp.txt", "w")
            fileTxt.write(text)
            fileTxt.close()

        jsonDict = {}
        for key in schemas.keys():
            if(DEBUG and key):
                print("key", key)
            data = schemas.get(key)
            jsonDict[key] = recurseveMap(None, data, text, jsonDict)
        docsJson.append(jsonDict)

    jsonTxt = json.dumps(docsJson, indent=4)

    outputFile = open("output/output.json", "w")
    outputFile.write(jsonTxt)
    outputFile.close()

    convert()
    print("\n[DONE]")


def recurseveMap(key, data, text, jsonDict):
    if(DEBUG and key):
        print("key", key)
    if(jsonDict):
        jsonDict = {}
    value = None
    if(isinstance(data, str)):
        regex = data
        searched = re.search(regex, text, re.IGNORECASE)
        if(searched):
            value = searched.group(1).strip()
    else:
        if 'list' in data:
            match = re.finditer(data["regex"], text, re.IGNORECASE)
            arrayTemp = []
            for m in match:
                arrayTemp.append(m.groupdict())
            value = arrayTemp
        else:
            value = {}
            for key in data.keys():
                value[key] = recurseveMap(key, data.get(key), text, value)
    return value


def removeAcentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def convert():
    print("Generated ok")
    return pd.read_json("output/output.json").to_excel("sheet/plan1.xlsx")


main()
convert()
