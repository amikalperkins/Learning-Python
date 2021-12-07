# L-System Rules for Strings
def applyRules(lhch):
    rhstr = ""
    if lhch == 'A':
        rhstr = 'B' # Rule 1
    elif lhch == 'B':
        rhstr = 'AB' # Rule 2
    else:
        rhstr = lhch # no rules apply so keep the character

    return rhstr

def processString(oldStr):
    newstr = ""
    for char in oldStr:
        newstr = newstr + applyRules(char)
    return newstr

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for iterator in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString

print(createLSystem(4, "B"))