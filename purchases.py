import re

from expense import *

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

    # return print(len(purchases))
    # return print(f"date: {purchases[0][0]}, amount: {purchases[0][1]}, desc: {purchases[0][2]}")
    # return print(purchases)
    return sort_purchases(purchases)

#categorize purchases and deposits
def sort_purchases(purchases):
    # expenses dictionary
    expenses = {"Food": 0, "Health": 0, "Rent": 0, "Transport": 0, "Car Insurance": 0, "Car Loan": 0,
                "Streaming": 0, "Internet": 0, "Student Debt": 0, "Phone": 0, "Laundry": 0, "Pet": 0, "Transfers": 0,
                "Other": 0}
    # list of expense categories and terms
    food_terms = ['cinnabon', 'bigy', 'pricerite', 'dollartree', 'olive', 'stop', 'elsafia', 'dd']
    streaming_terms = ['peacock', 'nbwn', 'netflix']
    rent_term = ['guardian']
    health_term = ['healthins']
    transportation_terms = ['uber', 'cumberland', 'pride', 'sunoco', 'nyx']
    car_ln_term = ['coastal']
    car_insr_term = ['hanover']
    intrnt_term = ['comcast']
    student_debt_term = ['studntloan']
    phone_term = ['metro']
    laundry_term = ['laundry']
    pet_term = ['petco']
    transfers_term = ['zelle', 'transfer']
    # search term list containing all categories
    search_terms = [food_terms, streaming_terms, rent_term, health_term, transportation_terms, car_ln_term,
                    car_insr_term, intrnt_term, student_debt_term, phone_term, laundry_term, pet_term, transfers_term]
    # terms to use to add amount to expenses dictionary
    add_terms = ["Food", "Streaming", "Rent", "Health", "Transport", "Car Loan", "Car Insurance", "Internet",
                 "Student Debt", "Phone", "Laundry", "Pet", "Transfers"]
    # get the amount of search terms in
    term_counter = 0
    for category in search_terms:
        category_len = len(category)
        term_counter+=category_len
    # print(term_counter)
    # for loop to go through each purchases
    for purchase in purchases:
        desc = purchase[2]
        amount = purchase[1]
        date = purchase[0]
        # print(date, desc, amount)
        counter = 0
        # for loop to go through each cat in sear term list
        for category in search_terms:
            # for loop to go through each term within each category
            for term in category:
                # finds description that matches term being loop through
                find = re.findall(term,desc.casefold())
                match find:
                    # if found, add amount to specific purchase category
                    case [term]:
                        # print("found")
                        cat_index = search_terms.index(category)
                        add_term = add_terms[cat_index]
                        # print(add_terms[cat_index])
                        s=""
                        for i in amount:
                            if i !=",":
                                s+=i
                                num=float(s)
                        expenses[add_term]+=num
                        break
                    # if not found, add amount to 'Other' category
                    case _:
                        counter+=1
                        s=""
                        if counter >= term_counter:
                            for i in amount:
                                if i != ",":
                                    s+=i
                                    num=float(s)
                            expenses["Other"]+=num
                            # print("not found")
                            # print(date,desc,amount)
                            # print(counter)
    # return print(expenses)
    return parse_expenses(expenses)