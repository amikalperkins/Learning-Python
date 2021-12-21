# Object-Oriented Programming 
# Defining Classes in Python

  # Euclid's Algorithm for fiding a greatest common divisor
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n 

        m = oldn
        n = oldm%oldn
    return n
    


class Fraction:

    # methods go here
    # the contructor defines the way in which data objects 
    # are created
    # constructor methods in python are always called __init__

    def __init__(self, top, bottom):
        self.numerator = top
        self.denominator = bottom

    # print method
    def show(self):
        print(self.numerator,'/', self.denominator)

    # ovveride built in string method with build in class methods
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

    
    # ovveride built in __add__ method
    def __add__(self, otherfraction):

        newnumerator = (self.numerator * otherfraction.denominator) + (self.denominator * otherfraction.numerator)
        newdenominator = (self.denominator * otherfraction.denominator)
        common = gcd(newnumerator,newdenominator)
        
        return Fraction(newnumerator, newdenominator)

    def __eq__(self, other):
        firstnumerator = self.numerator * other.denominator
        secondnumerator = other.numerator * self.denominator

        return firstnumerator == secondnumerator


myfraction = Fraction(3,4)

myfraction.show()
print(myfraction)