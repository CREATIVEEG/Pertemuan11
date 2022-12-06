#FUNGSI LAMBDA
import math

def a(x):
    return x ** 2
ac = lambda x : x ** 2
print(a(8))
print(ac(11))

def b(x, y):
    return math.sqrt(x**2 + y**2)
bc = lambda x, y :math.sqrt(x**2 + y**2)
print(b(1,4))
print(bc(2,5))

def c(*args):
    return sum(args)/len(args)
cc = lambda*args: sum (args)/len(args)
print(c(100,50))
print(cc(100,25))

def d(s):
    return "".join(set(s))
dc = lambda s :"".join(set(s))
print(d("ASU"))
print(dc("Hallo"))