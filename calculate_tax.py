# Taking income as input from the user
income = int(input("Enter your income: "))

# Initializing the tax_amount
tax_amount = 0

# Tax calculation based on income
if income <= 10000:
    tax_amount = 0
elif income <= 20000:
    x = income - 10000
    tax_amount = x * 10 / 100
else:
    tax_amount += (income - 20000) * 20 / 100
    # If income is above 20000, apply tax for the first 10000 as well
    tax_amount += 10000 * 10 / 100

# Printing the total tax to pay
print("Total tax to pay is", tax_amount)