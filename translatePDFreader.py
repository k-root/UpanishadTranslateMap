from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

class Meanings():
    def __init__(self, filePath):
        self.englishFilePath = filePath
    def splitPoints(self, englishTranslationFull):
        import re
        indexMatchList = re.finditer(r"(\d+\.)",englishTranslationFull)
        indexList=[]
        for index in indexMatchList:
            print(index.group())
            indexList.append(index.group())
        previousIndex="1."
        currentIndex=""
        bhavamDict = {}
        count=1
        start = englishTranslationFull.find(previousIndex)
        introduction = englishTranslationFull[:start]
        mantraTranslations = englishTranslationFull[start:]
        print(mantraTranslations)
        firstOccurance = indexList.index(previousIndex)
        indexListModified = indexList[firstOccurance+1:]
        for currentIndex in indexListModified:
            print("CURRENT INDEX1 :",currentIndex)
            if currentIndex in mantraTranslations:
                print("--CURRENT INDEX2--",currentIndex)
                split = mantraTranslations.split(currentIndex,1)
                bhavamDict[count] = split[0]
                mantraTranslations = split[1]
                print("FINAL MANTRA TRANSLATION: ", mantraTranslations)
            else:
                print(currentIndex, "Not in ", mantraTranslations)
            previousIndex = currentIndex
            count+=1
        lastMantra=""
        for finalLines in mantraTranslations.splitlines():
            if "Om! Peace! Peace! Peace!" not in finalLines:
                print("FINAL LINES: ", finalLines)
                lastMantra+=finalLines+"\n"
            end = "Om! Peace! Peace! Peace!\n"+mantraTranslations.split("Om! Peace! Peace! Peace!")[1]
        bhavamDict[count]=lastMantra
        bhavamDict["end"] = end
        return bhavamDict
    def getTextFromPDF(self):
        output_string = StringIO()
        with open(self.englishFilePath, 'rb') as in_file:
            parser = PDFParser(in_file)
            doc = PDFDocument(parser)
            rsrcmgr = PDFResourceManager()
            device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
        return output_string.getvalue()

if __name__ == "__main__":
    englishFilePath="Ishopanishat_English.pdf"
    englishMeanings = Meanings(englishFilePath)
    englishTranslationFull = englishMeanings.getTextFromPDF()
    bhavamDict = englishMeanings.splitPoints(englishTranslationFull)
