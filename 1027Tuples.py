from math import pi
# # Two types of sequential collections: strings
# # which are made up of characters; and lists
# # which are made up of elements of any type
# # lists are mutable strings are immutable
# # a tuple is similar to a list but they 
# # are immutable : syntactically a tupe is a 
# # comma seperated sequence of values and enclosed in 
# # parentheses even though it's not a requirement
# # tuples are usefule for what other languages call records: some
# # releated information that belongs together like a student record

# # tuple practice : a record of information that is immutable
# # but we can slice and concatenate just like strings

# julia = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
# # print(julia[2])
# # print(julia[2:6])

# # print(len(julia))

# # for field in julia:
# #     print(field)

# # julia = julia[:3] + ("Eat, Pray, Love", 2010) + julia[5:]
# # print(julia)

# # single field tuple (rare)
# # tup = (5,)
# # print(type(tup))

# # x = (5)
# # print(type(x))

# # Tuple Assignment
# # python has a powerful tuple assignment feature that allows
# # a tuple of variables on the left of an assignment to be assigned
# # values from a tuple on the right

# (name, surname, birth_year, movie, movie_year, profession, birth_place) = julia
# print(julia)
# print(julia[0])

# Tuples as Return Values
# this way we can return multiple elements inside a single tuple

def circleInfo(r):
    """ Return (circumference, area) of a circle with radius r"""
    c = (2. * 3.14159 * r)
    a = 3.14519 * (r*r)
    return (c,a)


tup = (circleInfo(10.0))
print(tup[0])
print(tup[1])

