import coffee_shop

print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)
print()

# Get some input from user
order_size = input("What size coffee would you like? ")
order_roast = input("What roast would you like? ")


# Send the order to the coffee shop module
shop_says = coffee_shop.order_coffee(order_size, order_roast)
# Print out what it gives back to us
print(shop_says)
print()

# See if customer wants to add milk
add_milk_response = input("Would you like to add milk (y/n)? ")
# Convert the response to lowercase, then check for a "yes" answer
if "y" in add_milk_response.lower():
    milk_fat = input("What percent milk do you want added? ")
    shop_says = coffee_shop.add_milk_please(milk_fat)
    # Print what it gave back to us
    print(shop_says)
