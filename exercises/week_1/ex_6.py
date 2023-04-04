"""exercise 6 week 1 on objects"""

# 6\. Edit the class defintion to add an instance attribute of is_hungry = True
# to the Dog class. Then add a method called eat() which changes the value of
# is_hungry to False when called. Figure out the best way to feed each dog
# and then output “My dogs are hungry.” if all are hungry or “My dogs are not
# hungry.” if all are not hungry. The final output should look like this:
#
# I have 3 dogs.
# Tom is 6.
# Fletcher is 7.
# Larry is 9.
# And they're all mammals, of course.
# My dogs are not hungry.


# Parent class
class Dog:
    """general dog object"""

    # Class attribute
    species = 'mammal'
    is_hungry = True

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        """return a string with general info of the dog"""
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        """return a string with what the dog says"""
        return f"{self.name} says {sound}"

    def eat(self):
        """change the status of is_hungry to False"""
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    """a species of dog"""

    def run(self, speed):
        """returns a string with the speed of the dog"""
        return f"{self.name} runs { speed}"


# Child class (inherits from Dog class)
class Bulldog(Dog):
    """a species of dog"""

    def run(self, speed):
        """returns a string with the speed of the dog"""
        return f"{self.name} runs {speed}"


def feed_all(dogs):
    """feed all the dogs"""
    for dog in dogs:
        dog.eat()


def check_hunger(dogs):
    """if they are hungry tells is"""
    hungry_dogs = 0
    not_hungry_dogs = 0
    for dog in dogs:
        if dog.is_hungry:
            hungry_dogs += 1
        elif not dog.is_hungry:
            not_hungry_dogs += 1
    if hungry_dogs == len(dogs):
        print("My dogs are hungry")
    elif not_hungry_dogs == len(dogs):
        print("My dogs are not hungry")
    else:
        print("not all hungry/not hungry")


# start my script
my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Flatcher", 7),
    Bulldog("Larry", 9)
]

print("I have ", len(my_dogs), " dogs")
for dog in my_dogs:
    print(dog.description())
check_hunger(my_dogs)
feed_all(my_dogs)
check_hunger(my_dogs)
