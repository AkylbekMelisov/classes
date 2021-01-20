class Car:
    wheels = 4
    def __init__(self,name,year,color,model,is_crashed):
        self.name = name
        self.year = year
        self.color = color
        self.model = model
        self.is_crashed = is_crashed
        self.fuel = 100
        self.run = 0
        self.speed = 0
        self.V = 20
        self.position = 0
        # print(f"{self.name} created!")


    def drive_to(self,city,km):
        result = self.V / 100
        result = result * km
        if result < self.fuel:
            self.fuel -= result
            if self.fuel >= 0:
                print(f"{self.name} drive to {city}")
        else:
            print('Road so far...')


    def charge(self):
        if self.fuel < 20:
            self.fuel = 100

    def crash(self,another_car):
        if self.position == another_car.position:
            self.is_crashed = True
            another_car.is_crashed = True
            print(f"{self.name} and {another_car.name} were crash!!!" )



class Human:

    def __init__(self,ful_name,age,heigth,weigth,nation):
        self.ful_name = ful_name
        self.age = age
        self.heigth = heigth
        self.weigth = weigth
        self.nation = nation
        self.position = 0
        self.health = 100
        self.is_live = True



    def move(self):
        self.position += 1


    def accident(self,car,trafficligt):
        if car.position == self.position and trafficligt.green:
            if self.health > 40:
                if 5 < car.speed < 20:
                    self.health -= 20
                elif car.speed > 20:
                    self.health -= 40
            else:
                self.is_live = False
            print(f"{self.ful_name} попал в аварию, его сбила {car.name}")





class Trafficlight:

    def __init__(self):
        self.red = False
        self.yellow = False
        self.green = False

    def set_color(self,color):
        if color == 'red':
           self.red = True
           self.yellow = False
           self.green = False
        elif  color == 'yellow':
            self.yellow = True
            self.red = False
            self.green = False
        elif color == 'green':
            self.green = True
            self.red = False
            self.yellow = False














audi = Car(name='AUDI',year=2021,color='grey',model='RX 8',is_crashed=False)
bmv = Car(name='BMV',year=2020,color='red',model='X 5',is_crashed=False)
honda = Car(name='HONDA',year=2020,color='red',model='X 5',is_crashed=False)

human1 = Human(ful_name='Bob',age=25,heigth=185,weigth=85,nation='france')

traffic_light = Trafficlight()
traffic_light.set_color('green')
print(traffic_light.red,traffic_light.yellow,traffic_light.green)

# audi.drive_to('Los-Angeles',1000)
# audi.crash(another_car=honda)
# # print(audi.is_crashed,bmv.is_crashed,honda.is_crashed)


bmv.speed = 50
human1.health = 41
human1.accident(bmv,traffic_light)
print('Здоровье человека: ',human1.health,'\n','Жив ли человек: ',human1.is_live)



