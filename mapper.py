import PyPDF2

englishFilePath="Ishopanishat_English.pdf"
samskrutamFilePath="Ishopanishat_Sanskrit.pdf"

# pdfFileObj = open("1.pdf", 'rb') 
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
# numPages = pdfReader.numPages
# print(pdfReader.getDocumentInfo())
# print(numPages) 

# for page in range(numPages):
#     pageObj = pdfReader.getPage(page)
#     # print(pageObj.extractText())
#     text1 = pageObj.extractText().encode('utf-8')
#     print(text1)
  
# # closing the pdf file object 
# pdfFileObj.close()
# from tika import parser
# raw = parser.from_file(englishFilePath)
# print(raw['content'])
from pdfminer import high_level

local_pdf_filename = englishFilePath
pages = [0] # just the first page

extracted_text = high_level.extract_text(local_pdf_filename, "", pages)
print(extracted_text)