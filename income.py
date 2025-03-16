def parse_income(income):
    # Total deposits
    total_deposits = sum(income.values())
    print("Total Deposits: $",total_deposits)
    total_deposits-=income['Savings Transfer']
    print("Deposits Minus Savings Transfers: $",total_deposits)
    trans_from_savings = income['Savings Transfer']
    print("Transfers From Savings: $", trans_from_savings)

    # income percentages
    income_percent = {}
    for key in income:
         income_percent[key] =f"{round(100 *  income.get(key,0) / total_deposits)}%"
    print("Income Percent: " ,income_percent)

    # expected, difference, and actual income
    expected_income = {'Tempus': 1200.00, "WGE": 2400.00, "Transfers": 0.00, "Other": 0.00, "Savings Transfer": 0.00}
    diff_income = {}
    for key in income:
        diff_income[key] = round(income[key] - expected_income.get(key, 0))
    print("Expected Income: ", expected_income)
    print("Difference in Income: ",diff_income)

    actual_income = {}
    for key in income:
        actual_income[key] = round(income.get(key, 0))
    print("Actual Income: ", actual_income)
