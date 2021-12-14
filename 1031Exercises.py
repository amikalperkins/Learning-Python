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

# def average(listOfNumbers):
#     sum = 0
#     for number in listOfNumbers:
#         sum = sum + number
#     return (sum//len(listOfNumbers))

# numberList = [1,2,3,4,5,6]
# print(average(numberList))

# def max(listOfNumbers):
#     maxValue = listOfNumbers[0]
#     for number in listOfNumbers:
#         if number > maxValue:
#             maxValue = number
#     return maxValue

# listNumbers = [5000,3,4,5,200,-2,2]
# print(max(listNumbers))

# def sum_of_squares(xs):
#     sum = 0
#     for element in xs:
#         sum = sum + (element ** 2)
#     return sum
# listOfNumbers = [2, 3, 4]
# # print(sum_of_squares(listOfNumbers))

# def countOdd(listOfNumbers):
#     count = 0
#     for element in listOfNumbers:
#         if element % 2 == 0:
#             count = count + 1
#     return count

# listOMania = [1,2,3, 4, 5, 6, 7]
# print(countOdd(listOMania))

# def count(lst):
#     newList = []
#     for element in lst:
#         if element == 'sam':
#             newList.append(element)
#             break
#         else:
#             newList.append(element)
#     return len(newList)

# listy = ['mike', 'sam', 'sara', 'levi', 'brock', 'sam']
# print(count(listy))

listy = [0,10,45,7,3]

# def reverseList(aList):
#     newList = []
#     for element in range(len(aList), 0, -1):
#         newList.append(element)
#     return newList

# print(reverseList(listy))

def insert(obj, index, aListy):
    newList = []
    for element in range(len(aListy)):
        if element == index:
            newList.append(obj)
        newList.append(aListy[element])
    return newList

print(insert('cat', 3, listy))