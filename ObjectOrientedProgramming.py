#############################CLASS#############################
class Car():
#############################METHOD#############################
  #this is method / method is inside of the function | 그리고 첫번째 argument는 method 에서 
  #python 에서는 instance!
  def start(self):
    print(self.doors)
    print("Start!")
  
  def __init__(self , **kwargs):
    self.wheels = 4
    self.windows = 4
    self.doors = 4
    self.seats = 4
    #color 를 찾을꺼고 없으면 black 이라고 하는거.
    self.color = kwargs.get("color" , "black")
    self.price = kwargs.get("price" , "not_free")
  def __str__(self):
    return "lalalalal"
  
###this is function###
  #def start():
  #  print("Start!")

###instance class###
  #my_car = Car()

###self###
  #python 은 metod 를 호출할때 그 method 의 instance 를 첫번째 argument 로 사용을함. self ! 
  #my_car.start(my_car) 이런식으로! 

##############################DIR##############################
  #dir 은 class 안에 있는 모든 것들을 list 로 보여줌.
  #print(dir(my_car))
  #__str__ => method 고 호출될 때 마다 그 class 의 instance 를 출력.
my_car = Car(color = "black" , price = "free")
print(my_car.color , my_car.price)

mini = Car()
print(mini.color , mini.price)

##############################EXTEND##############################
class Convertible(Car):
  
  def __init__(self , **kwargs):
    #super class 는 extend 했던 그 class  
    super().__init__(**kwargs)#함수이고 부모클래스를 호출가능! 호출하는함수!
    self.time = kwargs.get("time" , 10)

  def take_off(self):
    return "taking off"

  def __str__(self):
    return "Car with no roof"
open_car = Convertible()
print(open_car.color)