#! python3
# -*- utf-8 -*-

import PyPDF2, os

# it is quite hard to deal with PDF Files. Here we can see an example of dealing
# with PDFs, the extracted texts are not very useful in this IDLE.

os.chdir('/users/alex/desktop')
pdfFile = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print (reader.numPages)

page = reader.getPage(0)
print (page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())

# still, we can see that at a page level we can do some interesting things with
# PDFs, like in the example bellow.

pdfFile.close()

pdf1File = open('meetingminutes1.pdf', 'rb')
pdf2File = open('meetingminutes2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdf1File)
reader2 = PyPDF2.PdfFileReader(pdf2File)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('combinedminutes.pdf', 'wb')
writer.write(outputFile)

outputFile.close()

pdf1File.close()
pdf2File.close()
