import numpy as np
k=0
x=1
print x
while x<=3:#stop when x>3
    x=np.random.randn(1)
    print x
    k=k+1
    if k>5000:
        print "too many iterations:%d"%k
        break
if k<=5000:
    print "The first number >3 is %f"%x
    print "The number of iterations is %d"%k
