import re

from pdfminer.high_level import extract_text

EMAIL_REG = re.compile(r'[a-zA-Z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+')


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


def extract_emails(resume_text):
    return re.findall(EMAIL_REG, resume_text)


if __name__ == '__main__':
    text = extract_text_from_pdf('./cvs/cv.pdf')
    emails = extract_emails(text)

    if emails:
        print(emails[0]) # noqa: T001