# a = [1, 2, 3]
# b = a[:]
# b[0] = 5

# print(b)

# myList = [76, 92.3, "hello", True, 4, 76]
# myOtherList = []

# for items in myList[:3]:
#     myOtherList.append(items)

# for item in myList[3:]:
#     myOtherList = myOtherList + [item]

# myOtherList.append('apple')
# myOtherList.append(76)

# myOtherList.insert(3, "cat")
# myOtherList.insert(0, 99)
# print(myOtherList.index('hello'))
# print(myOtherList.count(76))

# print(myOtherList)
# myOtherList.remove(76)

# myOtherList.pop(myOtherList.index(True))

def average(listOfNumbers):
    sum = 0
    for number in listOfNumbers:
        sum = sum + number
    return (sum//len(listOfNumbers))

numberList = [1,2,3,4,5,6]
print(average(numberList))