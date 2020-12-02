import PyPDF2
import os

def pdfread(file):
    pdf = PyPDF2.PdfFileReader(file)
    return pdf

def addtowrite(pdf, writer):
    for i in range(pdf.getNumPages()):
        writer.addPage(pdf.getPage(i))

def merge(file1, file2, output):
    pdf1 = pdfread(file1)
    pdf2 = pdfread(file2)

    writer = PyPDF2.PdfFileWriter()

    addtowrite(pdf1, writer)
    addtowrite(pdf2, writer)

    writer.write(output)
    output.close()


if __name__ == '__main__':

    print("Merged file")

    file1 = open("Y:/Test Folder/mergetest/D-K-1931-0000001.pdf", 'rb')
    file2 = open("Y:/Test Folder/mergetest/D-K-1931-0000001-bk.pdf", 'rb')
    output = open("Y:/Test Folder/mergetest/OutputFolder/D-K-1931-0000001.pdf", 'wb')
    merge(file1, file2, output)
    output.close()
