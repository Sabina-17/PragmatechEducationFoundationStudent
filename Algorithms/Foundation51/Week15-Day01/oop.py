# void method
def Topla(a,b):
    # a ve b ededleri topla ve neticeni ekrana cap et
    print(a+b)
# return method
def Sum(a,b):
    # a ve b ededlerini topla ve yadinda saxla .. vaxt gelecek men ondan istifade edecem
    print(a+b)
    return a+b
    print('naber moruk')


def Func(a,b):
    c=a+b
    return c

def Func02(a,b):
    c=Func(a,b)
    if c%2==0:
        print('cutdur')
    else:
        print('tekdir')
    # Func methodunun icrasi neticesinde elde olunan deyerin tek ve ya cut oldugunu oyren


def Bar(a,b):

    print(a+b)

class PizzaAparati:
    def __init__(self):
        pass 
    def KalbasaElaveEt(self,_kalbasa):
        self.kalbasa=_kalbasa
    def PendirElaveEt(self,_pendir):
        self.pendir=_pendir


pizza=PizzaAparati()
print(pizza.kalbasa)
pizza.KalbasaElaveEt('1000Bereket')
pizza.PendirElaveEt('Westgold')

print(pizza.kalbasa)
print(pizza.pendir)

print(pizza) 