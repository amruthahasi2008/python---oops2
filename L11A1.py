from abc import ABC , abstractmethod
#Define the abstract Animal class inheriting from ABC. Add __init__(self, name, habitat) to store those two attributes. Add a display(self) method that prints name and habitat. Add an abstract speak(self) method with just pass as the body.
class Animal :
    # parent constructor
    def __init__(self, name , habitat):
        self.name = name
        self.habitat = habitat
    # concrete method
    def display(self) :
        print(f"Name :{self.name},habitat:{self.habitat}")
    # abstract method
    @abstractmethod
    def speak(self) :
        pass
    
#child class 1
class Dog(Animal) :
    def __init__(self, name, habitat,breed):
        super().__init__(name, habitat) # calls animal constructors
        self.breed = breed
    def speak(self) :
        print(f"{self.name} ,{self.breed} says woof woof!")

# child class 2
class Parrot(Animal):
    def __init__(self, name, habitat,phrase):
        super().__init__(name, habitat)
        self.phrase = phrase
    def speak(self):
        print(f"{self.name},says {self.phrase} {self.phrase}!")

# child class 3
class Lion(Animal) :
    def __init__(self, name, habitat,pride):
        super().__init__(name, habitat)
        self.pride = pride
    def speak(self):
        print(f"{self.name},Pride:{self.pride}says ROARRRR! ")
# creating objects and running
dog = Dog("Bruno","Home","Lab")
parrot = Parrot("Polly","jungle","squawk")
lion = Lion("simba","Savvanah","Pride Rock")

#Loop over [dog, parrot, lion] and for each animal call display() then speak(). Run the program and check all three animals print correctly.
print("---------ANIMAL SOUND SHOW----------")
for animal in [dog,parrot,lion]:
    animal.display()
    animal.speak()
    print()

    

