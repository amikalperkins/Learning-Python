def find(astring, achar):
    """
    find and return the index of achar in astring
    return -1 if achar does not occur in string
    """
    ix = 0
    found = False
    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix += 1
    if found:
        return ix
    else:
        return -1


print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))

