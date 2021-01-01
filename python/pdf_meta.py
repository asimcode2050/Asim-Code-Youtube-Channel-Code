from PyPDF4 import PdfFileReader
def pdf_meta(filename):
    with open(filename,'rb') as pdf:
        pdfFile = PdfFileReader(pdf)
        doc = pdfFile.getDocumentInfo()
        print(f'[***] PDF MetaData: {str(filename)}')
        for item in doc:
            print(f'[++] {item} : {doc[item]}')
pdf_meta('/home/asim/demo.pdf')