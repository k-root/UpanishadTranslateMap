from upanishadMantraTxtReader import UpanishadMantras
from translatePDFreader import Meanings

def writeToPdf(mantraMeaningCombined):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(5, 5)
    pdf.set_font('arial', '', 16.0)
    pdf.cell(ln=1, h=5, align='L', w=0, txt="UPANISHAD".strip(), border=0)
    pdf.ln()
    effective_page_width = pdf.w - 2*pdf.l_margin
    print(effective_page_width)

    pdf.add_font('gargi', 'B', 'gargi.ttf', uni=True) 
    pdf.cell(ln=0, h=5, align='L', w=0, txt="\n", border=0)
    for i in mantraMeaningCombined:
        pdf.ln()

        pdf.set_font('gargi', 'B', 15.0)
        for mantraLine in mantraMeaningCombined[i][0].splitlines():
        # print("ADDING SANSKRIT LINE: ", mantraMeaningCombined[i][0].strip())
            pdf.cell(ln=1, h=5, align='L', w=effective_page_width, txt=mantraLine.strip(), border=0)
        pdf.set_font('arial', '', 12.0)
        for translateLine in mantraMeaningCombined[i][1].splitlines():
            pdf.cell(ln=1, h=5, align='L', w=5, txt=translateLine.strip(), border=0)
    pdf.output('test.pdf', 'F')

def writeToTxt(mantraMeaningCombined):
    with open("MantraTranslateMapped.txt","wb") as f:
        for mantraIndex in mantraMeaningCombined:
            f.write(mantraMeaningCombined[mantraIndex][0].encode('utf-8'))
            f.write("\n".encode('utf-8'))
            f.write(mantraMeaningCombined[mantraIndex][1].encode('utf-8'))
            


if __name__ == "__main__":
    englishFilePath="Ishopanishat_English.pdf"
    mantrasTextFilePath = "Ishopanishat_Sanskrit.txt"
    englishMeanings = Meanings(englishFilePath)
    englishTranslationFull = englishMeanings.getTextFromPDF()
    print(englishTranslationFull)
    bhavamDict = englishMeanings.splitPoints(englishTranslationFull)

    reader = UpanishadMantras(mantrasTextFilePath)
    upanishadMantraFull = reader.readRawMantrasFromTxt()
    finalCleanMantras = reader.cleanUpMantra(upanishadMantraFull)
    mantraDict = reader.splitMantrasToIndex(finalCleanMantras)

    print("BHAVAM DICT: ",bhavamDict)
    print("MANTRA DICT: ",mantraDict)

    print(len(mantraDict),len(bhavamDict))

    mantraMeaningCombined = {}
    for index in mantraDict:
        if index in bhavamDict:
            mantraMeaningCombined[index] = [mantraDict[index],bhavamDict[index]]

    print("FINAL DICTIONALRY MAPPING: ", mantraMeaningCombined)
    writeToPdf(mantraMeaningCombined)
    writeToTxt(mantraMeaningCombined)