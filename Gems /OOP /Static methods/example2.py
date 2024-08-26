class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @staticmethod
    def from_birth_year(name, birth_year):
        current_year = 2024
        age = current_year - birth_year
        return Person(name, age)

# Create an instance using the static method
person = Person.from_birth_year('Alice', 1990)

print(person.name)  # Output: Alice
print(person.age)   # Output: 34
