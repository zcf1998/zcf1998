#implicit inheritance
'''
class parent(object):
    def implicit(self):
        print "parent implicit()"
        
class child(parent):
    pass

#explicitly override
class parent(object):
    def override(self):
        print "parent override()"

class child(parent):
    def override(self):
        print "children override()"
'''
#alter between the two vrsion
class parent(object):
    def altered(self):
        print "parent altered()"

class child(parent):
    def altered(self):
        print "child altered()"
        super(child,self).altered()
        
