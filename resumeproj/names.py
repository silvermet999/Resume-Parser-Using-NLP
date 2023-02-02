from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download("punkt")
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


pdf_path = './cvs/cv.pdf'


def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as fh:
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        pages = PDFPage.get_pages(fh)
        for page in pages:
            interpreter.process_page(page)
        text = retstr.getvalue()
    return text


def extract_text_from_pdf():
    txt = pdf_to_text(pdf_path)
    if txt:
        return txt.replace('\t', ' ')
    return None


def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                )

    return person_names


if __name__ == '__main__':
    text = extract_text_from_pdf()
    names = extract_names(text)

    if names:
        print(names[0])  # noqa: T001
