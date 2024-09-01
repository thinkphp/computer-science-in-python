class Parent:
    def __init__(self, name):
        print("call contructor from Parent")
        self.name = name

    def greeting(self):
        return f"Hello, I am {self.name} from Parent"

class Child( Parent ):

    def __init__(self, n, a):

        super().__init__( n ) #call __init__ de la class Parent

        self.age = a

    def greeting(self):

        parent_greeting = super().greeting() #call greeting din clasa parent

        return f"{parent_greeting} I am {self.age} years old"

ob = Child("David","10")
print( ob.greeting() )
