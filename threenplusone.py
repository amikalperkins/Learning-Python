def seq3np1(n,count): 
    """ print the 3n + 1 sequence from n, terminating when it reaches 1"""
    
    while n != 1:
        count += 1
        if n % 2 == 0: # n is even
            n = n // 2
        else : 
            n = n * 3 + 1
            
    return count
count = 0
print(seq3np1(7,count))

