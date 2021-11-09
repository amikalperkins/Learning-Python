# def squared(x):
#     return x*x

# toSquare = 10
# result = squared(toSquare)
# print("The result of {} squared is {}.".format(toSquare,result))

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal += x

    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of {} squared is {}".format(toSquare, squareResult))
