class Demo:
    value = 0

    def __init__(self, no1, no2):
        self.num1 = no1
        self.num2 = no2

    def fun(self):
        print(f"Inside instance method fun & values are {self.num1} and {self.num2}") 
    
    def gun(self):
        print(f"Inside instance method gun & values are {self.num1} and {self.num2}")

d_obj1 = Demo(11, 21)
d_obj2 = Demo(51, 101)

d_obj1.fun()
d_obj2.fun()

d_obj1.gun()
d_obj2.gun()