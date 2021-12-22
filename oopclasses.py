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
    
def lcm(a, b, c=1):
    if (a * c) % b !=0:
        return lcm(a, b, c+1)
    else:
        a * c

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

    # override built in string method with build in class methods
    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)

    
    # override built in __add__ method
    def __add__(self, otherfraction):

        newnumerator = (self.numerator * otherfraction.denominator) + (self.denominator * otherfraction.numerator)
        newdenominator = (self.denominator * otherfraction.denominator)
        common = gcd(newnumerator,newdenominator)
        
        return Fraction(newnumerator//common, newdenominator//common)
    
    # override __eq__ equality method check
    def __eq__(self, other):
        firstnumerator = self.numerator * other.denominator
        secondnumerator = other.numerator * self.denominator

        return firstnumerator == secondnumerator

    def multiply(self, otherfraction):
        multiplynumerator = self.numerator * otherfraction.numerator
        multiplydenominator = self.denominator * otherfraction.denominator

        return str(multiplynumerator)+'/'+str(multiplydenominator)

    def subtraction(self, otherfraction):
        # cross multiply
        newnumerator = (self.numerator * otherfraction.denominator) - (self.denominator * otherfraction.numerator)
        newdenominator = (self.denominator * otherfraction.denominator)
        common = gcd(newnumerator, newdenominator)

        return Fraction(newnumerator//common, newdenominator//common)

myfraction = Fraction(3,4)
myfraction2 = Fraction(4,5)


addFraction = myfraction.subtraction(myfraction2)
print(addFraction)