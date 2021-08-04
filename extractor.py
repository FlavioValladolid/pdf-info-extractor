import PyPDF2

# # pdf file object

pdfFileObj = open('test.pdf','rb')

# # pdf reader object

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# # number of pages in pdf

# print(pdfReader.numPages)

# # a page object

pageObj = pdfReader.getPage(0)

# # extracting text from page

infoPdf = pageObj.extractText()
line = infoPdf.split('\n')

for row in line:
    print(row)
