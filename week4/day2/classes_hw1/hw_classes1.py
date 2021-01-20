class Cat:

    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color
        self.tail = 'tail'

    def description(self):
        print(f"Имя: {self.name} возраст: {self.age} свет: {self.color}")


    def purr(self):
        print(f"{self.name} мурлычет!!!")

    def plays_with_tail(self):
        print(f"{self.name} ")

cat1 = Cat('Муся',3,'серый')




cat1.purr()


cat1.description()