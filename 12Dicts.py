# # """ Dictionaries are a collection of unordered items that
# # use key/value pairing using { key : value } """

# # # eng2spdict = {}

# # # eng2spdict['one'] = 'uno'
# # # eng2spdict['two'] = 'dos'
# # # eng2spdict['three'] = 'tres'

# # # print(eng2spdict['one'])

# # """ It doesn't matter what order we write the pairs. The values are associated with 
# # keys not indices """

# # """ del statement removes a key-value pair from a dictionary """

# # inventory = { 'apples' : 49 , 'banana' : 45 , 'pears' : 17 }
# # del inventory['pears'] # removes the key : value pair

# # """ they are mutable, instead of deleting pears, we could just set to 
# #  value to 0 """

# # inventory['pears'] = 0
# # print(inventory)

# # # adding to a value with key is similar to accumulator 

# # inventory['banana'] += 218
# # print(inventory)

# # print(len(inventory))

# # """ Dictionary methods: 
# # keys -> returns a view of the keys in the dictionary
# # values -> returns a view of the values in the dictionary
# # items -> returns a view of the key-value pairs in the dictionary
# # get(key) -> returns the value associated with the key
# # get(key,alt) -> returns the value associated with the key; alt otherwise
# # """

# # for key in inventory:
# #     print("Got key", key)

# grocerInventory = { 'apples': 345 , 'bananas' : 234, 'pears' : 34, 'oranges' : 256}
# print(list(grocerInventory.keys())) # create list with keys from dictionary
# print(list(grocerInventory.values())) # create list with values from dictionary

# # for (key, value) in grocerInventory.items():
# #     print("Got key->",key , "<-that maps to->",value)

# for key in grocerInventory:
#     print("Got key->", key, "<-that maps to->", grocerInventory[key])

""" Aliasing and Copying : since dictionaries are mutable, you need to be aware of 
aliasing.  Whenever two variables refer to the same dictionary object, chnages to one
affect the other """

opposites = {'up': 'down', 'right' : 'wrong', 'true': 'false'}
alias = opposites
print(alias is opposites)
alias['right'] = 'left'

print(opposites['right'])

""" if you want to make a copy of a dictionary without affecting the original 
use the method dictionary.copy() """

acopy = opposites.copy()
acopy['right'] = 'left' # does not affect original dictionary

