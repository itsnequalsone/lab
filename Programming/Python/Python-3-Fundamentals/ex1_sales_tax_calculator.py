"""Sales Tax Calculator"""

TAX = 0.06
amount = int(input("Enter an amount: "))
total = amount + amount*TAX
print(total)
