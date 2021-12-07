def count(text, aChar):
    lettercount = 0
    for char in text:
        if char == aChar:
            lettercount += 1
    return lettercount

print(count("banana", 'a'))