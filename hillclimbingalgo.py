""" Example of a algorithm in the class of Hill-Climbing (
    that is we only keep the result if it is better than 
    the previous one.)
How long do you think it would take for a Python
function to generate just one sentence of Shakespeare.
"""

# goal : "methinks it is like a weasel"

import random
def generateOne(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    result = ""
    for iterator in range(strlen):
        result = result + alphabet[random.randrange(27)]
    
    return result

def score(goal, teststring):
    numSame = 0
    sameLetters = ""
    for iterator in range(len(goal)):
        if goal[iterator] == teststring[iterator]:
            sameLetters = sameLetters + goal[iterator]
            numSame = numSame + 1
    return numSame / len(goal)



def main():
    goalstring = 'methinks it is like a weasel'
    newString = generateOne(28)
    best = 0
    newscore = score(goalstring, newString)
    while newscore < 1:
        if newscore >= best:
            print(newscore, newString)
            best = newscore
        newString = generateOne(28)
        newscore = score(goalstring, newString)

main()