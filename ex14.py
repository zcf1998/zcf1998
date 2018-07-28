import numpy as np
from sys import argv
script,r=argv
r=float(r)
def Cir(r): #calculate the circumference
    return 2*np.pi*r
C=Cir(r)
C_earth=Cir(6378.0) 
C_mars=Cir(3396.0)
if abs(C-C_earth)<abs(C-C_mars):
    print "more likely to be earth.%.16f"%(abs(C-C_mars)-abs(C-C_earth))
elif abs(C-C_earth)>abs(C-C_mars):
    print "more likely to be mars.%.16f"%(abs(C-C_mars)-abs(C-C_earth))
else:
    print "both are possible."
