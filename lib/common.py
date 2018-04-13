import json, os

class Json:

    def readFile2Obj(self, filePath):
        f_json = open(filePath, 'r')
        str_json = f_json.read()
        return json.loads(str_json)

    def readCatalog2List(self, catalogPath):
        lsResult = []
        files = os.listdir(catalogPath)
        for fr_file in files:
            filePath = catalogPath + '/' + fr_file
            dic_json = self.readFile2Obj(filePath)
            lsResult.append(dic_json)
        return lsResult