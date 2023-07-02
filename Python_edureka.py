# print("hello from Python Edureka chapter")
# ##Comparison Operator
# print(2>3) ##result will be boolean that is false
# print(2<=3)##resut will be a boolean that is true
# ##Logical Operators
# age = 18
# print(age>1 and age<20)##this will use logical operator AND and return true
# print(age>89 or age<2) ##False)
# print(not age>2) ##using the not operator
# ##and both true
# ##or atleast 1 true
# ##not
# ##Augmented Assignment
# x = 10
# # x = x+30
# print(x+=10)
# ##Better way
# y = 10
# y+=30
# print(y)
# if (y>=100):
#     print("printing from 1st loop")
#     print("Leaving the team like that")
# elif (y>=3 and y<=50):
#     print("Second loop testing")
# i=0
# j =1
# while i<=100:
#     while j<=1000:
#         print(j)
#         j+=100
#     print(i)
#     i+=1
# i=0
# j=0
#
# while i<10:
#     while j<20:
#         print('#'*j)
#         j+=1
#     j=0 #Resetting the J counter for correct printing
#     i+=1
# help(print)

##Data structures
# names  = ['ELTON','JOHN','NAME']
# print(names)
# print(names[0:1])
# help(list)
##for Loop example
i = 0
a=[]
x =10
for x in range(10):
    a.append(i)
    i+=1
for i in a:
    print(i)
print(a)

# Creating a tuple
tuple = (1, 2, 3, 'a', 'b', 'c')

# Accessing elements in a tuple
print(tuple[0])  # Output: 1
print(tuple[3])  # Output: 'a'

# Slicing a tuple
print(tuple[2:5])  # Output: (3, 'a', 'b')

# Length of a tuple
print(len(tuple))  # Output: 6

# Iterating over a tuple
for element in tuple:
    print(element)

# Tuple unpacking
a, b, c = tuple[:3]
print(a, b, c)  # Output: 1 2 3

# Concatenating tuples
new_tuple = tuple + ('x', 'y', 'z')
print(new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 'x', 'y', 'z')




