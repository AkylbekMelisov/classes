class Car:

    def __init__(self,mark, color,model,year):
        self.mark = mark
        self.color = color
        self.model = model
        self.year = year
        self.run = 0

    def move(self,distance:int):
        if distance > 0:
            self.run += distance

car1 = Car('bmv','back','x6','2020')
car2 = Car('mercedes','pink','s 600','2021')
car3 = Car('tesla','white','S 6','2021')
car3.move(240)
print(car3.mark,car3.model,car3.run)
car3.move(-240)
print(car3.mark,car3.model,car3.run)
