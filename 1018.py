# # """
# # for each word in WORDS, add 'd' to the end of the word if 
# # the word ends in 'e' to make it past_tense. Otherwise, add
# # 'ed' to make it past tense.  Save these past_tense words to 
# # a list called past_tense
# # """
# # words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]
# # past_tense = []
# # for word in words:
# #     if word[-1] == 'e':
# #         past_tense.append(word + 'd')
# #     else:
# #         past_tense.append(word + 'ed')

# # print(past_tense)

# # Using Lists as Parameter in this case you are actually 
# # going to change the list itself, LISTS are mutable
# # def doubleStuff(aList):
# #     """ Overwrite each element in aList with double its value"""
# #     for position in range(len(aList)):
# #         aList[position] = aList[position] * 2

# # things = [2, 5, 9]
# # print(things)
# # doubleStuff(things)
# # print(things)

# # using lists as  PURE FUNCTION pure functions do not mutate
# # the original object.  Instead they return a value 

# def doublePureStuff(a_list):
#     """ Return a new list without modifying the original"""
#     new_list = []
#     for iterator in a_list:
#         new_element = 2 * iterator
#         new_list.append(new_element)
#     return new_list

# things = [2, 5, 9]
# print(things)
# things = doublePureStuff(things)
# print(things)

""" Functions that Produce Lists
add to your toolbox pattern:

initialize a result variable to be an emtpy list
loop
    create a new element
    append it to result
return the result

"""

def primes_upto(n):
    """ Return a list of all prime numbers less than n"""
    new_list = []
    for item in range(2, n):
        if is_prime(item):
            new_list.append(item)
    return new_list