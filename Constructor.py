"""class constructor:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.fullname=self.fname+" "+self.lname
obj1=constructor('Raquib','Mahamud')
print(obj1.fullname)"""
class dog:
    def __init__(self,breed,name,spots):
        self.breed=breed
        self.name=name
        self.spots=spots
obj1=dog("ply","tom",spots="no spots")
print(obj1.name)

