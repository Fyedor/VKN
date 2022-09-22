import math
def func (d):
    y = (math.sin(d+4)-math.cos(3*d))/(math.sqrt(5*d))+math.log(math.fabs(d+4),2)
    return (y)
x = int(input("Ввети x:"))
y = func(x)
print (y)