import numpy as np
r=raw_input("Please input the radius of the earth(6378000)\n")
r=float(r);
C=2*np.pi*r
S=4*np.pi*r**2
print "The circumference of the earth is:\n\t",C,"\nThe surface area of the earth is:\n\t",S #print result
