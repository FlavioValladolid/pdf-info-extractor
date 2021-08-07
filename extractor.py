import PyPDF2
from PyPDF2.utils import isInt

def pdfReader_(path):
    pdfReader = PyPDF2.PdfFileReader(path)
   
    # # number of pages in pdf

    # print(pdfReader.numPages)

    # # a page object

    pageObj = pdfReader.getPage(0)

    # # extracting text from page

    infoPdf = pageObj.extractText()
    line = infoPdf.split('\n')

    a = []
    for row in line:
        try:
            if 'HTS#' in row:
                row = row.split(' ')
                for item in row:
                    a.append(int(item))
            if 'colors' in row:
                row = row.strip()
                row = row.split('  ')
                for item in row:
                    a.append(item)
        except:
            pass

    return a
