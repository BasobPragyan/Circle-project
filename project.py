class circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        print("Perimeter of circle is : ",2*3.14*self.radius)
    def area(self):
        print("Area of circle is : ",3.14*self.radius**2)

rad=int(input("Enter radius : "))
c1=circle(rad)
c1.perimeter()
c1.area()