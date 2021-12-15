""" Write a program that takes a string counts the number
of each char and then prings a table of those items"""

def stringCount(str):
    counts = {}
    for element in str:
        counts[element] = str.count(element)
    return counts




stringInput = input("Please enter a sentence: ")
countss = stringCount(stringInput)

for (key, value) in countss.items():
    print("{} {}".format(key, value))
