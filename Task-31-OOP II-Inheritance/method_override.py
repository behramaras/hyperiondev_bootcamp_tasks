# The code has a class namely Adult as a parent class. And has another class namely Child as a child class.

# The Adult class is created. Adult class has 4 attributes which are name, age, eye_colour, hair_colour.
# The Adult class also has a method namely 'can_drive'.
# The 'can_drive' method prints the name of the person and that they are old enough to drive.

class Adult:
    def __init__(self, name, age, eye_colour, hair_colour):
        self.name = name
        self.age = age
        self.eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"\n{self.name.capitalize()} is old enough to drive.\n")


# The Child class is created. Child class inherits from the Adult class.
# The Child class has a method namely 'can_drive'. The can_drive method is overrided in this class.
# The 'can_drive' method prints the name of the person and that they are too young to drive.

class Child(Adult):
    def __init__(self, name, age, eye_colour, hair_colour):
        super().__init__(name, age, eye_colour, hair_colour)

    def can_drive(self):
        print(f"\n{self.name.capitalize()} is too young to drive a car.\n")


# The code takes a name, an age, an eye colour and a hair colour as an input from the user.
# And determines if the person is 18 or older and creates an instance of the Adult class if this is true.
# Otherwise, it creates an instance of the Child class. And prints whether the person is driving or not with their name.

while True:

    option = input("\t\tWelcome to the driver program\nEnter 0 to quit or enter another character to continue: ")

    if option != "0":
        name = input("Enter your name: ")
        
        while True:
            try:
                age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Please enter a number!\n")
                continue
            
        hair_colour = input("Enter your hair colour: ")
        eye_colour = input("Enter your eye colour: ")

        if age >= 18:
            adult_person = Adult(name, age, eye_colour, hair_colour)
            adult_person.can_drive()

        else:
            young_person = Child(name, age, eye_colour, hair_colour)
            young_person.can_drive()

    else:
        break
