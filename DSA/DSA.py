new_list = [1,2,3,4,5,6]
print(new_list)
new_list.pop(2)
print(new_list )

for x in new_list:
    print(x)
#Dictionary
a = {1: "Hello", 2: "World"}
print(a)
a.clear() #will delete elements from the dictionary
print(a)


b = {1: "Hello", 2: "World", 3: "Again", 4: "Your"}
print(b)
b.pop(2) #Element present at index 2 i.e index 2 present as value will be deleted
print(b) #The popitem() method removes the item that was last inserted into the dictionary.
# In versions before 3.7, the popitem() method removes a random item.
# The removed item is the return value of the popitem() method, as a tuple, see example below.

print(b.popitem())
print(b)
print(b.popitem())
print(b)
print(b.popitem())
print(b)

c = {1: "Python", 2: "Java", 3: "C#"}
print(c[1])
print(c.get(3))


##Tuple

my_tuple = (1,2,3,4,4,5)
print(my_tuple)
y = tuple((1,2,3,4,7))
print(y)
print(y.count(2))
empty_tuple = ()
print(empty_tuple)

#Using for loop access the elements of a Tuple

for i in my_tuple:
    print(i)


#Sets are unordered collection of Unique elements
#Sets are mutable but contains only Unique elements
#Sets are defined by putting elelemts inside {}

simple_set = {1,2,2,3,4,4,5,6,7}
print(simple_set)
#As you can see duplicate elements were remove inside the simple_set

for i in simple_set:
    print(i)

simple_set.add(8)
simple_set.add(65)
print(simple_set)
#for reference simple_set = {1,2,2,3,4,4,5,6,7,8,65}
my_set = {11,12,13,14,15,65}

unionset = simple_set|my_set

print(unionset) #Using | will remove the duplicate entries in the set: Unionset
#The same operation can be done by using union function

print(simple_set.union(my_set))
#Also can do the intersection as well

print(simple_set.intersection(my_set))
#Will return 65 as it's the only common value
print("End Of Part")

#Algorithms:


#Trees

class Node:
    def __init__(self,val):
        self.lc = None
        self.rc = None
        self.nodedata = val

root = Node(1)
root.lc = Node(2)
root.rc = Node(3)
root.lc.lc = Node(4)
root.lc.rc = Node(5)

def Inorder(root):
    if root:
        Inorder(root.lc)
        print(root.nodedata)
        Inorder(root.rc)
Inorder(root)

print("------------------------------------------------------------------------------------------------------------------------")

def preorder(root):
    if root:
        print(root.nodedata)
        preorder(root.lc)
        preorder(root.rc)

preorder(root)
print("------------------------------------------------------------------------------------------------------------------------")
def postorder(root):
    if root:
        postorder(root.lc)
        postorder(root.rc)
        print(root.nodedata)

print("------------------------------------------------------------------------------------------------------------------------")

postorder(root)