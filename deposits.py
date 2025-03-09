import re

from income import *

# get deposits from pdf file: (date, amount, desc.)
def parse_deposits(pdf_text):
    text = pdf_text
    keyword_one = re.search("Credits", text)
    keyword_two = re.search("Daily", text)

    span_value_one = keyword_one.span()
    span_value_two = keyword_two.span()
    text_section = text[span_value_one[0]: span_value_two[1]]

    deposit_pattern = "(\d{2}/\d{2})((?:\d{1},)?(?:\d{1})?[0-9]+\.\d{2})((?:[0-9]+[a-zA-z]+-)?([a-zA-Z]+))"
    deposits = re.findall(deposit_pattern, text_section)
    # return print(len(deposits))
    return sort_deposits(deposits)

def sort_deposits(deposits):
    income = {"Tempus": 0, "WGE": 0, "Transfers": 0, "Other": 0, "Savings Transfer": 0}
    search_terms = ['tempus', 'city', 'zelle', 'savings']
    search_dict = {'tempus':0, 'city':0, 'zelle':0, "other": 0, 'savings': 0}
    for deposit in deposits:
        desc = deposit[2]
        amount = deposit[1]
        date = deposit[0]
        print(date,desc,amount)
        counter = 0
        for term in search_terms:
            find = re.findall(term,desc.casefold())
            match find:
                case [term]:
                    s=""
                    for i in amount:
                        if i !=",":
                            s+=i
                            num = float(s)
                    search_dict[term]+=num
                    break
                case _:
                    counter+=1
                    if counter == 4:
                        s=""
                        for i in amount:
                            if i !=",":
                                s+=i
                                num=float(s)
                        search_dict["other"]+=num
    income["Tempus"]+=search_dict["tempus"]
    income["WGE"]+=search_dict["city"]
    income["Transfers"]+=search_dict["zelle"]
    income["Other"]+=search_dict["other"]
    income["Savings Transfer"]+=search_dict["savings"]
    return parse_income(income)