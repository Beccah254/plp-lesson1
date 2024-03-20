class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Create an instance of the Person class
person1 = Person("Becky", 25, "female")
person2 = Person("Vinny", 30, "male")

# Call the introduce method to display the person's information
person1.introduce()
person2.introduce()