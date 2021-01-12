class UpanishadMantras():
    def __init__(self, filePath):
        self.filePath = filePath
    def readRawMantrasFromTxt(self):
        with open(self.filePath,'rb') as f:
            upanishadMantraFull = f.read()
        return upanishadMantraFull.decode('utf-8-sig')

    def cleanUpMantra(self, upanishadMantraFull):
        finalCleanMantras = ''
        for line in upanishadMantraFull.splitlines():
            if len(line)>=1:
                finalCleanMantras+=line+"\n"
        return finalCleanMantras
    
    def splitMantrasToIndex(self, finalCleanMantras):
        import re
        indexMatchList = re.finditer(r"\॥(\s\S*)\॥",finalCleanMantras)
        indexList=[]
        for index in indexMatchList:
            indexList.append(index.group())

        mantraDict = {}
        mantraDictNumericIndex = {}
        count=1
        for mantraIndex in indexList:
            if mantraIndex in finalCleanMantras:
                split = finalCleanMantras.split(mantraIndex)
                mantraDict[mantraIndex] = split[0]
                mantraDictNumericIndex[count]=split[0]
                finalCleanMantras = split[1]
                count+=1

        return mantraDictNumericIndex

if __name__ == "__main__":
    reader = UpanishadMantras("Ishopanishat_Sanskrit.txt")
    upanishadMantraFull = reader.readRawMantrasFromTxt()
    finalCleanMantras = reader.cleanUpMantra(upanishadMantraFull)
    mantraDict = reader.splitMantrasToIndex(finalCleanMantras)
