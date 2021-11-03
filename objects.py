# #type function displays object type

# print(type("hello, world!")); #string
# print(type(17));
# print(type(42000));

# # type conversion
# print(3.13, int(3.14));


# # Names assigned to objects are variables

# firstName = "Brad";
# print(firstName);

# # assignment statement

# message = "What's up doc?";
# n = 17;
# pi = 3.14;
# print(message);

# expressions
minutes = 645;
hours = minutes / 60;
print(hours);

print(10**2); # 10 to the second power

# division will make a floating point /
# for integer division // 
# modulus operator % gives remainder
myNumber = 10;
print(myNumber % 2 == 0);

total_secs = 7684;
hours = total_secs // 3600; # int division
secs_still_remaining = total_secs % 3600;
minutes = secs_still_remaining // 60;
secs_finally_remaining = secs_still_remaining % 60;
print("Hrs=", hours, "mins=", minutes, "secs=", secs_finally_remaining);