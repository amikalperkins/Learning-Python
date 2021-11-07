import coffee_shop

print("Welcome to", coffee_shop.shop_name)
print("Available sizes:", coffee_shop.coffee_sizes)
print("Available roasts:", coffee_shop.coffee_roasts)

# Get some input from user
order_size = input("What size coffee would you like? ")
order_roast = input("What roast would you like? ")

# Send the order to the coffee shop module
shop_says = coffee_shop.order_coffee(order_size, order_roast)

# Print out what it gives back to us
print(shop_says)