""" A matrix is a two dimensional collection, typically thought of having 
rows (i) and columns (j) of data """

""" One way to do this is with a list of lists"""

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

# the above example is called a sparse matrix
# since there is no reason to store all of the zeroes
# this method is inefficient and we can use a dict with tuples

matrix = {(0,3): 1, (2,1): 2, (4,3): 3}

# we only need three key-value pairs, one for each nonzero element of the matrix
# each key is a tuple and each value is an integer
# to access an element of the matrix, we could use the [] operator

matrix[(0,3)]
print(matrix.get((0,3)))
print(matrix.get((3,1), 0))

