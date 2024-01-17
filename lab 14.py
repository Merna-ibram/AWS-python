import json
import jsonFileHandler

def readJsonFile(fileName):
    data = jsonFileHandler.readJsonFile('files/insulin.json')
    try:
        with open(fileName) as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return data

