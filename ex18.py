class organism(object):
    def __init__(self):
        self.breath=True
        self.cell=True


class animal(organism):
    def __init__(self):
        super(animal,self).__init__()
        self.move=True
        self.eat=True

class vertebrate(animal):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spine=True
        self.magic=False

class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.viviparity=True
        self.eggs=False
    def egg(self):
        print "mammals don't have eggs."

class dog(mammal):
    def __init__(self):
        super(dog,self).__init__()
        self.run=True
        self.fly=False
    def cannotfly(self):
        print "Dogs can't fly."
