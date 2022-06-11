import textract
import PyPDF2

#open and read text from file of pdf extension
def extract_text_from_pdf(file):
    fileReader = PyPDF2.PdfFileReader(open(file,'rb'))
    page_count = fileReader.getNumPages()
    text = [fileReader.getPage(i).extractText() for i in range(page_count)]
    return str(text).replace("\\n", "")

#open and read text from file of pdf extension
def extract_text_from_word(filepath):
    txt = textract.process(filepath).decode('utf-8')
    return txt.replace('\n', ' ').replace('\t', ' ')