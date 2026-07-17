class Circle:
    PI = 3.14

    def __init__(self, radius = 0, area = 0, circumFerence = 0):
        self.r = radius
        self.a = area
        self.c = circumFerence

    def accept_radius(self):
        self.r = float(input("Enter the radius of circle: "))
        return self.r
    
    def calculate_area(self):
        area = Circle.PI * (self.r ** 2)
        self.a = area
        return self.a
    
    def calculate_circumference(self):
        circumference = 2 * Circle.PI * self.r
        self.c = circumference
        return self.c
    
    def display(self):
        print(f"Radius of circle is: {self.r}")
        print(f"Area of circle is: {self.a:.2f}")
        print(f"Circumference of circle is: {self.c:.2f}")

print("-------------- Calculate Area & Circumference of Circle --------------")
print("-" * 70)

c_obj1 = Circle()
c_obj1.accept_radius()
c_obj1.calculate_area()
c_obj1.calculate_circumference()
c_obj1.display()

print("-" * 70)

c_obj2 = Circle()
c_obj2.accept_radius()
c_obj2.calculate_area()
c_obj2.calculate_circumference()
c_obj2.display()

print("-" * 70)

c_obj3 = Circle()
c_obj3.accept_radius()
c_obj3.calculate_area()
c_obj3.calculate_circumference()
c_obj3.display()

print("-------------- Calculate Area & Circumference of Circle --------------")