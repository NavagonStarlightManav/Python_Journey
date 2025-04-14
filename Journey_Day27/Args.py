def add(*args):
    print(args[0])
    sum=0
    for n in args:
        sum+=n
    return sum

print(add(10,20,30,50))

def calculate(n,**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
        print(key)
        print(value)
    n+=kwargs['add']
    n*=kwargs['nancy']
    print(n)


calculate(1,add=3,nancy=59)

class Car:
    def __init__(self,**kw):
        self.make=kw.get('make')
        self.model=kw['model']
        self.colour=kw.get('color')
        self.year=kw.get('year')

my_car=Car(model="GT-B",color="green")
print(my_car.make)
print(my_car.colour)
