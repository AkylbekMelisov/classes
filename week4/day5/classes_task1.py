class Employee:

    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary


    def __add__(self, other):
        return (self.salary + other.salary) / 2


emp1 = Employee(name='Tramp',age=74,salary=500)
emp2 = Employee(name='Baiden',age=78,salary=600)

print(emp1 + emp2)