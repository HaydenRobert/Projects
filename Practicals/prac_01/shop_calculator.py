running_total = 0
number_of_items = int(input("Number of items: "))
if number_of_items < 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
else:
    for i in range(number_of_items):
        item_price = float(input("Price of item: "))
        running_total += item_price
    if running_total > 100:
        running_total *= 0.9
    print("Total price for", number_of_items, "items is", running_total)