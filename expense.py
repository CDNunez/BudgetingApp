import math

def parse_expenses(expense):
    # total withdrawals
    total_expenses = sum(expense.values())
    print("Total Withdrawals: $", total_expenses)

    #withdrawal percentage
    expense_percent = {}
    for key in expense:
        expense_percent[key] = f"{round(100*expense.get(key,0)/total_expenses)}%"
    print("Expense Percent: ", expense_percent)

    #expected, difference, and actual expense
    expected_expense = {"Food": 320, "Health": 50, "Rent": 1350, "Transport": 400, "Car Insurance": 265, "Car Loan":
        369, "Streaming": 64, "Internet": 70, "Student Debt": 235, "Phone": 129, "Laundry": 50, "Pet": 40,
                        "Transfers": 0, "Other": 0}
    diff_expense = {}
    for key in expense:
        diff_expense[key] = round(expense[key] - expected_expense.get(key,0))
    print("Expected Expenses: ", expected_expense)
    print("Difference in Expenses: ", diff_expense)

    actual_expenses = {}
    for key in expense:
        actual_expenses[key]=math.ceil(expense.get(key,0))
    print("Actual Expnses: ", expense)