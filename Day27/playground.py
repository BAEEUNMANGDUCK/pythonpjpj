# advanced arguments 

# unlimited (positional) arguments ==> 가변 인자
def add(*args):
    '''*args는 값들이 튜플로 묶임'''
    sum = 0 
    for num in args:
        sum += num
    
    return sum


answer = add(1,2,3,4,5)
print(answer)
    

# **kwargs


def calculate(n, **kwargs):
    # print(type(kwargs))
    print(kwargs)
    
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)



calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self,**kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")
        

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)        
print(my_car.make)        