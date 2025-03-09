import math

def parse_income(income):
    total_deposits = sum(income.values())
    print("Deposits & Credits: $",total_deposits)
    total_deposits-=income['Savings Transfer']
    print("Deposits: $",total_deposits)
    tempus = math.floor(income["Tempus"])
    print(tempus)
    trans_from_savings = income['Savings Transfer']
    return print("Income",income)