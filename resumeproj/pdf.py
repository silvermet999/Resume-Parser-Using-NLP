from pdfminer.high_level import extract_text


def extract_text_from_pdf():
    return extract_text("./cvs/cv.pdf")



if __name__ == '__main__':
    print(extract_text_from_pdf()) # noqa: T001