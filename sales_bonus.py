"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    price = sales * 0.1
    print("You get a 10% bonus and you will get $",float(price))
else:
    price = sales * 0.15
    print("You get a 15% bonus and you will get $",float(price))
