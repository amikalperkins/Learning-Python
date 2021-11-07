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
    return "Here's your {} coffee roasted {}.".format(size, roast)

def add_milk_please(fat_content):
    """
    Give an option to add milk
    : parameter fat_content : a string or integer containing the milkfat content
    : return : a message about having added milk
    """
    return "We have added {}% milk you requested.".format(fat_content)

def give_tip(tip_amount):
    """
    Take a tip from the user, then be happy about it
    : parameter tip_amount : the tip amount
    : return : nothing
    """
    print("Thank you so much! We don't make a ton of money.")
    
    # Not having a return statement defaults to None

