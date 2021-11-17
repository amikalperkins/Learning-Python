def newtSqrt(n, howmany):
    approx = 0.5 * n
    for iterator in range(howmany):
        betterapprox = 0.5 * (approx + n/approx)
        print(betterapprox)
        approx = betterapprox
    return betterapprox

print(newtSqrt(100,10))
