"""
How to grab all the text from PDF files in Python using PyPDF2
YouTube Channel: Asim Code
https://youtu.be/IJU4gjCu0Jg
"""
import PyPDF2

pdf_file  = open('sample.pdf','rb')
list_text = []
pdf_read = PyPDF2.PdfFileReader(pdf_file)
for page_num in range(pdf_read.numPages):
    page = pdf_read.getPage(page_num)
    list_text.append(page.extractText())

print(list_text)
