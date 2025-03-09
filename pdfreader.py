from io import StringIO
from pdfminer.high_level import extract_text_to_fp

from deposits import *
from purchases import *

# step 2
# extract text from pdf
def extract_pdf_text(pdf_path):
    #variable to store PDF
    text = StringIO()
    # extract text from PDF into variable as a string
    with open(pdf_path, 'rb') as fin:
        extract_text_to_fp(fin, text)
    # call on subsequent funcs: get purchases, get  deposits, etc
    # pass pdf text to funcs
    return parse_purchases(text.getvalue().strip()), parse_deposits(text.getvalue().strip())