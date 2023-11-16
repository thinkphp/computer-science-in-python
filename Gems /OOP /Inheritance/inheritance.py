# clasa de baza Person
class Person:
      #constructorul clasei
      def __init__(self, name, age):
          self.name = name
          self.age = age

      #o metoda
      def birthday(self):
           print("Happy birthday you were", self.age)
           self.age += 1
           print("Now you are", self.age)
# O noua clasa Employee care extinde clasa de baza Person
class Employee( Person ):

      def __init__(self, name, age, id):
          self.id = id
          super().__init__(name, age)
          #se apeleaza constructorul definit la
          #linia 4


      def calculate_pay(self, hours_worked):
          rate_of_pay = 7.50
          if self.age >= 21:
              rate_of_pay += 2.50

          return hours_worked * rate_of_pay

class SalesPerson( Employee ):
      def __init__(self, name, age, id, region, sales):
          super().__init__(name,age,id)
          self.region = region
          self.sales = sales
      def bonus(self):
          return self.sales * 0.5

def main():
    #am creat un obiect p
    p = Person("Dustin", 49)
    print(p)
    print('_'*55)

    #am creat al obiect e
    e = Employee("Diaz", 40, 1234)#se apeleaza instructiunea de la linia 16
    e.birthday()
    print('e.calculate_pay(40)', e.calculate_pay(78))
    print('_' * 55)
main()
