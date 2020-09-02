num_of_items = int(input("Number of items: "))
#Get the number
total_price = 0
for i in range(1, num_of_items+1):
    the_price_of_item = float(input("Price of items: "))
    #Get the price
    total_price += the_price_of_item

if total_price > 100:
#Decided range
   total_price *= 0.9
print("Total price for ", num_of_items, "items is", total_price)
#Next loop