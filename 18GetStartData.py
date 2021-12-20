# float_radius = float(input("Please enter the radius of a circle: "))
# print(type(float_radius))

# diameter = 2 * float_radius
# print(type(diameter))

wordlist = ['cat', 
            'dog', 
            'rabbit']
# outer loop is the list of words 0 cat, 1 dog, 2 rabbit
# inner loop iterates over the characters 0 [0,1,2] 
#                                         1 [0,1,2] 
#                                         2 [0,1,2,3,4,5]
letterlist = set([aletter for aword in wordlist for aletter in aword])

# sets do not allow duplicates
# and then convert back to a list
# for aword in wordlist:
#     for aletter in aword:
#         if aletter not in letterlist:
#             letterlist.append(aletter)

print((list(letterlist)))