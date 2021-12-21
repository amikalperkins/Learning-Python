# Newton's Method for approximating square roots
# newguess = (1/2) * (oldguess + (n/oldguess))

def squareroot(n):
    root = (n/2)
    for k in range(20):
        root = (1/2) * (root + (n/root))
    return root

print(squareroot(9))
