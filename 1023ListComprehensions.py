# """ List comprehensions are conscise ways to create lists.
#     General Syntax is as follows:
#     [<expression> for <item> in <sequence> if <condition>]
# """

# # myList = [1, 2, 3, 4, 5]
# # your_list = [item ** 2 for item in myList if item % 2 == 0]
# # print(your_list)
# # # this will print your list inside a []

# """ Strings and Lists """
# # using split creates a list then to use .join() 
# # to recreate the string.join()
# song = "The rain in Spain..."
# wds = song.split() # space is delimeter
# print(wds)

# songs = "The rain in Spain..."
# wdss = songs.split('ai') # ai is the delimeter word boundary
# # this will git rid of the 'delimeter'
# print(wdss)

# # the inverse of split is the join method.  Choose a desired separator string
# # often called the 'glue' and the join the list with the glue between 
# # each of the elements

# wdsss = ["red", "blue", "green"]
# glue = ';'
# s = glue.join(wdsss)
# print(s)

# print(wdsss)

# print("***".join(wdsss))

# list type conversion
xs = list("Crunchy Frog")
stringxs = ''.join([str(element) for element in xs])
print(stringxs)