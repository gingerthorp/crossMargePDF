from PyPDF2 import PdfFileReader, PdfFileWriter


def crossMargePDF(pdf_name1, pdf_name2):
    # Use a breakpoint in the code line below to debug your script.

    file_name = pdf_name2.split('.')[0]

    pdf_1 = PdfFileReader(open(pdf_name1, "rb"))
    pdf_2 = PdfFileReader(open(pdf_name2, "rb"))

    # output pdf create
    output = PdfFileWriter()

    for page in range(pdf_1.getNumPages()):
        page_1 = pdf_1.getPage(page)
        page_2 = pdf_2.getPage(page)

        output.addPage(page_1)
        output.addPage(page_2)

    output_stream = open(f"{file_name}_cross.pdf", "wb")
    output.write(output_stream)
    output_stream.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pdf_file1 = "3_Lecture Note 1.en.ko.pdf"
    pdf_file2 = "3_Lecture Note 1.pdf"

    crossMargePDF(pdf_file1, pdf_file2)
