class Employee:

    amount = 1.1

    def __init__(self,first,last,email,salary):
        self.first = first
        self.last = last
        self.email = email
        self.salary = salary


    def total_amount(self):
        print(self.salary * self.amount)


class Developer(Employee):

    amount = 1.2

    def __init__(self,first,last,email,salary,prog_lang):
        super().__init__(first,last,email,salary)
        self.prog_lang = prog_lang
        self.is_remote = True



class Manager(Employee):

    amount = 1

    def __init__(self,first,last,email,salary,employers=None):
        super().__init__(first,last,email,salary)
        if employers is None:
            self.employers = []
        else:
            self.employers = employers


    def recruit(self,employer):
        if employer not in self.employers:
            self.employers.append(employer)


    def delete_employer(self,employer):
        if employer in self.employers:
            self.employers.remove(employer)

    def show_employers(self):
        for employer in self.employers:
            print(employer)



class Designer(Employee):

    amount = 1.1

    def __init__(self,first,last,email,salary,portfolio=None):
        super().__init__(first,last,email,salary)
        if portfolio is None:
            self.portfolio = []
        else:
            self.portfolio = portfolio
            if len(portfolio) > 20:
                Designer.amount = 1.5

    def show_portfoplio(self):
        for picture in self.portfolio:
            print(picture)



emp1 = Employee(first='Maksim',last='Surovkin',email='maksim@gmail.com',salary=100)

emp1.total_amount()

dev1 = Developer(first='Nurjanat',last='Abaeva',email='abaeva@gmail.com',salary=100,prog_lang='python')
dev1.total_amount()

mng1 = Manager(first='Aigerim',last='Kashkarbekova',email='kashkarbekova@gmail.com',salary=10000,employers=['Nurjanat','Baiel','Aigerim'])
mng1.total_amount()
mng1.recruit('jarkynai')
print(mng1.employers)

mng1.delete_employer('Nurjanat')
print(mng1.employers)

mng1.show_employers()

dsg1 = Designer(first='Baiel',last='Nurmatbek uulu',email='baiel@gmail.com',salary=16000,portfolio=('youtobe','google','pycharm'))
dsg1.show_portfoplio()
dsg1.total_amount()