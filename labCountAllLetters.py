def countAll(str):
    counts = {}
    for element in str:
        counts[element] = (str.count(element))
    return(counts)
myString = 'bbbbbanana'
print(countAll(myString))