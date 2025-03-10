I'll explain how to apply the SOLID principles in Python 3 with examples for each principle.

## 1. Single Responsibility Principle (SRP)

A class should have only one reason to change, meaning it should have only one responsibility.

```python
# Bad: Class has multiple responsibilities
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def save(self):
        # Save user to database
        print(f"Saving user {self.name} to database")
    
    def send_email(self, message):
        # Send email to user
        print(f"Sending email to {self.name}: {message}")

# Better: Separate responsibilities into different classes
class User:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

class UserRepository:
    def save(self, user):
        # Save user to database
        print(f"Saving user {user.get_name()} to database")

class EmailService:
    def send_email(self, user, message):
        # Send email to user
        print(f"Sending email to {user.get_name()}: {message}")
```

## 2. Open/Closed Principle (OCP)

Software entities should be open for extension but closed for modification.

```python
# Bad: Need to modify class to add new shapes
class AreaCalculator:
    def calculate_area(self, shape):
        if hasattr(shape, 'width') and hasattr(shape, 'height'):
            return shape.width * shape.height
        elif hasattr(shape, 'radius'):
            return 3.14 * shape.radius ** 2
        else:
            raise ValueError("Shape not supported")

# Better: Use polymorphism to extend functionality
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()
```

## 3. Liskov Substitution Principle (LSP)

Objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program.

```python
# Bad: Square is not a proper substitute for Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_width(self, width):
        self.width = width
        self.height = width  # Violates LSP
    
    def set_height(self, height):
        self.width = height  # Violates LSP
        self.height = height

# Better: Use a common abstraction
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def area(self):
        return self.side_length ** 2
```

## 4. Interface Segregation Principle (ISP)

No client should be forced to depend on methods it does not use.

```python
from abc import ABC, abstractmethod

# Bad: Fat interface
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

# Classes must implement all methods, even if they don't need them
class Robot(Worker):
    def work(self):
        print("Robot is working")
    
    def eat(self):
        # Robots don't eat, but have to implement this
        pass
    
    def sleep(self):
        # Robots don't sleep, but have to implement this
        pass

# Better: Segregated interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human is working")
    
    def eat(self):
        print("Human is eating")
    
    def sleep(self):
        print("Human is sleeping")

class Robot(Workable):
    def work(self):
        print("Robot is working")
```

## 5. Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on abstractions.

```python
# Bad: High-level module depends on low-level module
class MySQLDatabase:
    def connect(self):
        print("Connected to MySQL database")
    
    def query(self, sql):
        print(f"Executing query: {sql}")

class UserService:
    def __init__(self):
        self.database = MySQLDatabase()  # Direct dependency
    
    def get_user(self, user_id):
        self.database.connect()
        self.database.query(f"SELECT * FROM users WHERE id = {user_id}")

# Better: Both depend on abstractions
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def query(self, sql):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL database")
    
    def query(self, sql):
        print(f"Executing query: {sql}")

class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL database")
    
    def query(self, sql):
        print(f"Executing SQL: {sql}")

class UserService:
    def __init__(self, database: Database):  # Dependency injection
        self.database = database
    
    def get_user(self, user_id):
        self.database.connect()
        self.database.query(f"SELECT * FROM users WHERE id = {user_id}")
```

These examples demonstrate how to apply each SOLID principle in Python. The key points to remember are:

- Single Responsibility: Each class has one job
- Open/Closed: Extend functionality without modifying existing code
- Liskov Substitution: Subtypes must be substitutable for their base types
- Interface Segregation: Create specific interfaces rather than general ones
- Dependency Inversion: Depend on abstractions, not concrete implementations
