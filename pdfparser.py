import PyPDF2


def get_string_from_pdf(pdf_path):
    content = ""
    p = open(pdf_path, 'rb')
    pdfReader = PyPDF2.PdfFileReader(p)
    if pdfReader.isEncrypted:
        pdfReader.decrypt('')
    end_page = pdfReader.getNumPages()
    # print (pdfReader.numPages)
    for pageNum in range(0, 1): #end_page
        page = pdfReader.getPage(pageNum)
        if page.extractText() is not None:
            pageContents = page.extractText()
            content += pageContents
    return content