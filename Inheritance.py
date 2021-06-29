"""class phone:
    def call(self):
        print("you can call")
    def message(self):
        print("you can message")
class samsong(phone):
    def photo(self):
        print("you can can take photo")
s = samsong()
s.call() """
class shape:
    def __init__ (self,dim1,dim2):
        self.dim1=dim1
        self.dim2=dim2
    def area (self):
        print("I am the area method of shape class")
class triangle(shape):
    def area (self):
        area= .5 * self.dim1 * self.dim2
        print("area of trangle",area)
class rectangle(shape):
    def area (self):
        area= self.dim1 * self.dim2
        print("area of rectangle",area)
t1=triangle(5,6)
t1.area()
t2=rectangle(10,25)
t2.area()
