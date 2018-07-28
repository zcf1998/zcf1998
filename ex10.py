import numpy as np
def Cir(r,name):
    C=2*np.pi*r
    print "The circumference of %s is %f."%(name,C)

def dif(a,b):
    return a-b

a=raw_input("input float1\n")
a=float(a)
b=raw_input("input float2\n")
b=float(b)
c=dif(a,b)
print "%f"%c    
Cir(6378,"Earth")
Cir(3396,"Mars")
