""" Dictionaries are a collection of unordered items that
use key/value pairing using { key : value } """

# eng2spdict = {}

# eng2spdict['one'] = 'uno'
# eng2spdict['two'] = 'dos'
# eng2spdict['three'] = 'tres'

# print(eng2spdict['one'])

""" It doesn't matter what order we write the pairs. The values are associated with 
keys not indices """

""" del statement removes a key-value pair from a dictionary """

inventory = { 'apples' : 49 , 'banana' : 45 , 'pears' : 17 }
del inventory['pears'] # removes the key : value pair

""" they are mutable, instead of deleting pears, we could just set to 
 value to 0 """

inventory['pears'] = 0
print(inventory)