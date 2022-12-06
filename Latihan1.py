#FUNGSI LAMBDA (Rhendy Diki Nugraha)
import math

def a(x):
    return x ** 2
ac = lambda x : x ** 2
print(a(4))
print(ac(10))

def b(x, y):
    return math.sqrt(x**2 + y**2)
bc = lambda x, y :math.sqrt(x**2 + y**2)
print(b(2,4))
print(bc(6,9))

def c(*args):
    return sum(args)/len(args)
cc = lambda*args: sum (args)/len(args)
print(c(20,75))
print(cc(55,90))

def d(s):
    return "".join(set(s))
dc = lambda s :"".join(set(s))
print(d("Hallo"))
print(dc("Hai"))