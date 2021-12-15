""" Working with Data Files """

# for line in myFile:
#     statement1
#     statement2
#     ....

# reading files with a for loop

# readfile = open("text.txt", "r") # open text file for reading

# for alineinfile in readfile:
#     values = alineinfile.split() # parses data at spaces
#     # creates a list with values = [] 
#     # values[0] values[1] tokens etc

# readfile.close() # must close file

# using a while loop

#  readfile = open("text.txt", "r")
#  line = line.readline() # reading each line priming a true. if no line
#  won't begin loop
#  while line: # while true meaning there are lines
#     values = line.split()
#      now they've been parsed into a list named values
#        line.readline() # assigns line to the next line to read.  change of state
#         # otherwise an infinite loop would occur because first line read would always
#         be true and never move to another line

# # readfile.close() 

# with Statements
# syntax
# with <create some object that understands context> as <some name>:
    # do some stuff with the object
