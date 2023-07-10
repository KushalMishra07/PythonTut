# # print("hello from Python Edureka chapter")
# # ##Comparison Operator
# # print(2>3) ##result will be boolean that is false
# # print(2<=3)##resut will be a boolean that is true
# # ##Logical Operators
# # age = 18
# # print(age>1 and age<20)##this will use logical operator AND and return true
# # print(age>89 or age<2) ##False)
# # print(not age>2) ##using the not operator
# # ##and both true
# # ##or atleast 1 true
# # ##not
# # ##Augmented Assignment
# # x = 10
# # # x = x+30
# # print(x+=10)
# # ##Better way
# # y = 10
# # y+=30
# # print(y)
# # if (y>=100):
# #     print("printing from 1st loop")
# #     print("Leaving the team like that")
# # elif (y>=3 and y<=50):
# #     print("Second loop testing")
# # i=0
# # j =1
# # while i<=100:
# #     while j<=1000:
# #         print(j)
# #         j+=100
# #     print(i)
# #     i+=1
# # i=0
# # j=0
# #
# # while i<10:
# #     while j<20:
# #         print('#'*j)
# #         j+=1
# #     j=0 #Resetting the J counter for correct printing
# #     i+=1
# # help(print)
# 
# ##Data structures
# # names  = ['ELTON','JOHN','NAME']
# # print(names)
# # print(names[0:1])
# # help(list)
# ##for Loop example
# i = 0
# a=[]
# x =10
# for x in range(10):
#     a.append(i)
#     i+=1
# for i in a:
#     print(i)
# print(a)
# 
# # Creating a tuple
# tuple = (1, 2, 3, 'a', 'b', 'c')
# 
# # Accessing elements in a tuple
# print(tuple[0])  # Output: 1
# print(tuple[3])  # Output: 'a'
# 
# # Slicing a tuple
# print(tuple[2:5])  # Output: (3, 'a', 'b')
# 
# # Length of a tuple
# print(len(tuple))  # Output: 6
# 
# # Iterating over a tuple
# for element in tuple:
#     print(element)
# 
# # Tuple unpacking
# a, b, c = tuple[:3]
# print(a, b, c)  # Output: 1 2 3
# 
# # Concatenating tuples
# new_tuple = tuple + ('x', 'y', 'z')
# print(new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 'x', 'y', 'z')
# 
# my_dict = {"name": "K", "age": 22, "city": "New York"}
# 
# # Accessing values in a dictionary
# print(my_dict["name"])  # Output: K
# print(my_dict["age"])   # Output: 22
# 
# # Modifying values in a dictionary
# my_dict["age"] = 32
# print(my_dict["age"])   # Output: 32
# 
# # Adding a new key-value pair
# my_dict["occupation"] = "Analyst"
# print(my_dict)          # Output: {"name": "John", "age": 32, "city": "New York", "occupation": "Analyst"}
# 
# # Removing a key-value pair
# del my_dict["occupation"]
# print(my_dict)          # Output: {"name": "John", "age": 32, "occupation": "Engineer"}
# 
# # Checking if a key exists in a dictionary
# print("name" in my_dict)  # Output: True
# print("occupation" in my_dict)  # Output: False
# 
# # Getting the number of key-value pairs in a dictionary
# print(len(my_dict))     # Output: 3
# 
# # Iterating over key-value pairs in a dictionary
# for key, value in my_dict.items():
#     print(key, ":", value)
##Changing the value of a tuple -
# a = (1,2,3,4,[2,3,4])
# print(a)
# a[4][2] = 6
# print(a)
# ##Hence changed the values of tuple
# ##If trying to change other values:
# # a[2] = 2 ##throws an error
# ##You can concatenate using + addition symbol
# b = (5,6,7,8,9) #Tuple a already assigned
# c = a+b
# print(c)
# ##You can use del keyword to delete a tuple
# print(c)
# # del c
# # print(c) ##C gets deleted
# print(c.count(2)) #It will give the number of times 2 has been repeated in the tuple c
# print(c.index(4))##a.index will return the index of value inside the tuple also if the number is repeated then
# #                returns the index of the first occurence of that number

#


