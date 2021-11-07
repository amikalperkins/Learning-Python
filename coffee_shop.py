"""
The coffee shop module contains functions and contains variables
important to implementing a coffee shop
"""
# Set some variables
shop_name = "Runestone Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]

def order_coffee(size, roast):
    """
    Take an order from a user
    : parameter size: a string containing one of the coffee sizes
    : parameter roast: a string containing one of the coffee roasts
    : return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {}".format(size, roast)