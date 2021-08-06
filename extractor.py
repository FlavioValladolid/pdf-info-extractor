import PyPDF2

# # pdf file object

# pdfFileObj = open('test.pdf','rb')

# # pdf reader object

pdfReader = PyPDF2.PdfFileReader(r'C:\Users\Flavio\Documents\SMK Python Projects\PDF info extractor\test.pdf')

# # number of pages in pdf

# print(pdfReader.numPages)

# # a page object

pageObj = pdfReader.getPage(0)

# # extracting text from page

infoPdf = pageObj.extractText()
line = infoPdf.split('\n')

print(line.index(' '))
# for row in line:
#     print(row)
