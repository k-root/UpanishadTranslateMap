from upanishadMantraTxtReader import UpanishadMantras
from translatePDFreader import Meanings

def writeToPdf(upanishadName, mantraMeaningCombined):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_xy(5, 5)
    pdf.set_font('arial', '', 16.0)
    pdf.cell(ln=1, h=5, align='L', w=0, txt=upanishadName.strip(), border=0)
    pdf.ln()
    effective_page_width = pdf.w - 2*pdf.l_margin
    print(effective_page_width)

    pdf.add_font('gargi', 'B', 'gargi.ttf', uni=True) 
    pdf.cell(ln=0, h=5, align='L', w=0, txt="\n", border=0)
    count =1
    for i in mantraMeaningCombined:
        pdf.ln()
        pdf.set_font('gargi', 'B', 15.0)
        for mantraLine in mantraMeaningCombined[i][0].splitlines():
        # print("ADDING SANSKRIT LINE: ", mantraMeaningCombined[i][0].strip())
            pdf.cell(ln=1, h=5, align='L', w=effective_page_width, txt=mantraLine.strip(), border=0)
        pdf.set_font('arial', '', 12.0)

        pdf.cell(ln=0, h=5, align='L', w=5, txt=str(count)+".   ", border=0)
        
        # for translateLine in mantraMeaningCombined[i][1].splitlines():
        pdf.multi_cell(h=5, align='L', w=0, txt=mantraMeaningCombined[i][1].strip(), border=0)
        count+=1
    pdf.output(upanishadName+'UpanishadMapped.pdf', 'F')

def writeToTxt(mantraMeaningCombined):
    with open(upanishadName+"UpanishadMantraTranslateMapped.txt","wb") as f:
        count=1
        for mantraIndex in mantraMeaningCombined:
            f.write(mantraMeaningCombined[mantraIndex][0].encode('utf-8'))
            f.write("\n".encode('utf-8'))
            f.write((str(count)+". ").encode('utf-8') + mantraMeaningCombined[mantraIndex][1].encode('utf-8'))
            f.write("\n".encode('utf-8'))
            count+=1
            


if __name__ == "__main__":
    upanishadName = "Adhyatma Upanishad"
    englishFilePath="{}.pdf".format(upanishadName)
    mantrasTextFilePath = "{}_Sanskrit.txt".format(upanishadName)
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
    writeToPdf(upanishadName, mantraMeaningCombined)
    writeToTxt(mantraMeaningCombined)