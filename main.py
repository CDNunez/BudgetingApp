import re
from operator import index
# from pdfminer.high_level import  extract_text

import os
from dotenv import load_dotenv

from io import StringIO
from pdfminer.high_level import extract_text_to_fp

# //TODO: parse purchases by date(mm/dd), amount, desc
# //TODO: parse deposits by date(mm/dd), amount, desc
# //TODO: assign category to purchases
# //TODO: assign category to deposits
# //TODO:

load_dotenv()

PDF = os.getenv('PDF')
PDF_two = os.getenv('PDF_two')

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
    return parse_purchases(text.getvalue().strip())

# step 3
# get purchases from pdf file: {date, amount, desc.}
def parse_purchases(pdf_text):
    text = pdf_text
    # due to how bank statements are formatted, purchases can be found between these two keywords
    #the program will use the span func to find the index of these keywords and slice needed data
    keyword_one = re.search("Purchases", text)
    keyword_two = re.search("Credits", text)
    #text section where purchase data is found in PDF file
    span_value_one = keyword_one.span()
    span_value_two = keyword_two.span()
    text_section = text[span_value_one[0]:span_value_two[1]]

    # pattern to find date within doc
    transaction_pattern = "(\d{2}/\d{2})((?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})"
    transactions = re.findall(transaction_pattern,text_section)

    # description_pattern = "(?:(?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})?[a-zA-Z](?:\d{2}/\d{2})?"
    # descriptions = re.findall(description_pattern,text_section)

    purchase_pattern = "(\d{2}/\d{2})((?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})((?:[0-9]+)?[a-zA-Z]+)"
    purchases = re.findall(purchase_pattern,text_section)

    return print(purchases)

# step 1
#Main function to run program once PDF file is dropped into application
def main_parse_function(pdf_file_path):
    # call extract func passing through  PDF file path to the func
    extract_pdf_text(pdf_file_path)

main_parse_function(PDF)