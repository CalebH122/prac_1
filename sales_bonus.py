"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    amount_of_sale = int(input("Please enter your sale amount: "))
    while amount_of_sale > 0:
        if amount_of_sale < 1000:
            bonus = amount_of_sale * 0.1
            print("You bonus is: {}".format(bonus))
            amount_of_sale = int(input("Please enter your sale amount: "))
        elif amount_of_sale >= 1000:
            bonus = amount_of_sale * 0.15
            print("Your bonus is: {}".format(bonus))
            amount_of_sale = int(input("Please enter your sale amount: "))
    print("Your sale amount should > 0")


main()
