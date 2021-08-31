import json


class EditConfig:
    def __init__(self, temp=''):
        self.__filepath = temp

    def readConfig(self):
        try:
            with open(self.__filepath) as f:
                return json.load(f)
        except:
            return None

    def addGesture(self, val=''):
        try:
            jsonDict = self.readConfig()
            jsonDict['count'] += 1
            jsonDict['curId'] += 1
            jsonDict['gesture'][jsonDict['curId']] = val
            with open(self.__filepath, 'w') as f:
                json.dump(jsonDict, f, indent=4)
                return True
        except:
            return False

    def delGesture(self, val=''):
        try:
            jsonDict = self.readConfig()
            jsonDict['count'] -= 1
            for i, j in jsonDict['gesture'].items():
                if j == val:
                    del jsonDict['gesture'][i]
                    break
            with open(self.__filepath, 'w') as f:
                json.dump(jsonDict, f, indent=4)
            return True
        except:
            return False

    def viewConfig(self):
        try:
            JsonDict = self.readConfig()
            print(json.dumps(JsonDict, indent=4))
        except:
            print("Invalid Json String")

    def writeConfig(self, x):
        try:
            with open(self.__filepath, 'w') as f:
                json.dump(x, f, indent=4)
        except:
            print("Invalid Json String")
