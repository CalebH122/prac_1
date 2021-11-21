TOTAL_PRICE = 0
number_of_item = int(input("Please the number of items you have purchased: "))
while number_of_item <= 0:
    print("Invalid input")
    number_of_item = int(input("Please the number of items you have purchased: "))
    
for i in range(1, number_of_item + 1):
    item_price = float(input("Item price: "))
    TOTAL_PRICE = TOTAL_PRICE + item_price

if TOTAL_PRICE > 100:
    TOTAL_PRICE = TOTAL_PRICE - TOTAL_PRICE * 0.1
    print("Your total price for {} items is {}".format(number_of_item, TOTAL_PRICE))
else:
    print("Your total price for {} items is {}".format(number_of_item, TOTAL_PRICE))
