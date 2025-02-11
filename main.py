import re

import os
from dotenv import load_dotenv

from io import StringIO
from pdfminer.high_level import extract_text_to_fp

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
    return parse_purchases(text.getvalue().strip()), parse_deposits(text.getvalue().strip())

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

    # captures (two-digit month/two-digit year)(transaction amount up to 00,00.00)(captures num if present,
    # captures description, dash or num if interrupted, then continues to capture description )
    purchase_pattern = ("(\d{2}/\d{2})((?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})((?:[0-9]+)?[a-zA-Z]+(?:\*)?(?:-[0-9]+)?("
                        "?:-[a-zA-Z]+)?("
                        "?:[a-zA-Z]+"
                        ")?)")
    # finds date, amount, description based on purchase pattern above
    purchases = re.findall(purchase_pattern,text_section)

    return print(len(purchases))
    # return print(f"date: {purchases[0][0]}, amount: {purchases[0][1]}, desc: {purchases[0][2]}")
    # return print(purchases)
    # return sort_purchases(purchases)

# get deposits from pdf file: (date, amount, desc.)
def parse_deposits(pdf_text):
    text = pdf_text
    keyword_one = re.search("Credits", text)
    keyword_two = re.search("Daily", text)

    span_value_one = keyword_one.span()
    span_value_two = keyword_two.span()
    text_section = text[span_value_one[0]: span_value_two[1]]

    deposit_pattern = "(\d{2}/\d{2})((?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})([a-zA-Z]+)"
    deposits = re.findall(deposit_pattern, text_section)
    # return print(len(deposits))
    return sort_deposits(deposits)

#step 4
#categorize purchases and deposits
def sort_purchases(purchases):
    expenses = {"Food": 0, "Health": 0, "Rent": 0, "Transport": 0, "Car Insurance": 0, "Car Loan": 0,
                "Streaming": 0, "Internet": 0, "Student Debt": 0, "Phone": 0, "Laundry": 0, "Pet": 0, "Transfers": 0,
                "Other": 0}
    search_terms = ["peacock", "nbwn", "netflix", "cumberland", "sunoco", "nyx", "laundry", "dd", "cinnabon",
                    "pricerite", "bigy", "dollartree", "olive", "uber", 'cinemark', 'amazon', 'comcast',
                    'stop', 'cvs', 'petco', 'feverup', 'elsafia', 'pride', 'platinumnorth', 'usps', 'zelle',
                    'clubfees', 'guardian', 'coastal', 'hanover', 'studntloan', 'healthins', 'metro']
    for purchase in purchases:
        desc = purchase[2]
        for term in search_terms:
            found = re.findall(term,desc.casefold())
            if found:
                s = ""
                amount_string = purchase[1]
                for i in amount_string:
                    if i != ",":
                        s+=i
                        floated = float(s)
                        num = int(floated)
                if found == ['peacock'] or found == ['nbwn'] or found == ['netflix']:
                    expenses["Streaming"]+=num
                elif (found == ['sunoco'] or found == ['cumberland'] or found == ['pride'] or found == ['uber'] or
                      found) ==['nyx']:
                    expenses["Transport"]+=num
                elif found == ["laundry"]:
                    expenses["Laundry"]+=num
                elif (found == ["dd"] or found ==["pricerite"] or found == ["bigy"] or found == ['dollartree'] or
                      found ==["stop"] or found == ['cvs'] or found == ['elsafia']):
                    expenses["Food"]+=num
                elif found == ["healthins"]:
                    expenses["Health"]+=num
                elif found == ["coastal"]:
                    expenses["Car Loan"]+=num
                elif found == ["studntloan"]:
                    expenses["Student Debt"]+=num
                elif found == ["hanover"]:
                    expenses["Car Insurance"]+=num
                elif found == ['comcast']:
                    expenses["Internet"]+=num
                elif found == ["metro"]:
                    expenses["Phone"]+=num
                elif found == ['guardian']:
                    expenses["Rent"]+=num
                elif found == ["petco"]:
                    expenses["Pet"]+=num
                elif found == ["zelle"]:
                    expenses["Transfers"]+=num
                else:
                    expenses["Other"]+=num
    return print(expenses)


def sort_deposits(deposits):
    income = {"Tempus": 0, "WGE": 0, "Transfers": 0, "Other": 0}
    search_terms = ['tempus', 'city', 'zelle']
    for deposit in deposits:
        desc = deposit[2]
        for term in search_terms:
            found = re.findall(term,desc.casefold())
            if found:
                s = ""
                amount_string = deposit[1]
                for i in amount_string:
                    if i != ",":
                        s+=i
                        num = float(s)
                if found == ['tempus']:
                    income["Tempus"]+=num
                elif found == ['city']:
                    income["WGE"]+=num
                elif found == ['zelle']:
                    income['Transfers']+=num
                else:
                    income['Other']+=num
                # print(f"search term loop: {found, deposit[1], search_terms.index(term),num, income}")
        # print("deposit loop: ",deposit[2])
    return parse_income(income)

def parse_income(income):
    return print(income)

# step 1
#Main function to run program once PDF file is dropped into application
def main_parse_function(pdf_file_path):
    # call extract func passing through  PDF file path to the func
    extract_pdf_text(pdf_file_path)

main_parse_function(PDF)