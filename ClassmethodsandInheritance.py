#Basic Classes Example

class dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = dog('lab','Dog')

print(sam.species)
print(sam.breed)

#Methods example
class circle():
    pi = 3.14
    def __init__(self,radius = 7):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*self.pi



mycircle = circle(20)
print(mycircle.radius)
print(mycircle.area())

#Inheritance
class animal():
    def __init__(self):
        print("animal created")
    def report(self):
        print("Animal")
    def eat(self):
        print("Eating")

a = animal()
a.eat()
a.report()
# Creating another class Dog which will inherit Animal Properties

class dog(animal):
    def __init__(self):
        animal.__init__(self)
        print("Dog Created")
#Also defining methods exlusive for dog class
    def message(self):
        print("The above Eating and animal result is coming from Parent class - Animal")
#You can also override a parent class method in child classs
#Instance of Dog class
#Change one
d = dog()
d.eat()
d.report()
d.message()
#Change two
#Change three
