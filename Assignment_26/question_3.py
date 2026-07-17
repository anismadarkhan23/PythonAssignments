class ArithmeticOperations:
    def __init__(self, num1 = 0, num2 = 0):
        self.value1 = num1
        self.value2 = num2

    def addition(self):
        return self.value1 + self.value2
    
    def substraction(self):
        return self.value1 - self.value2
    
    def multiplication(self):
        return self.value1 * self.value2
    
    def division(self):
        try:
            return self.value1 / self.value2
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")

class Arithmetic(ArithmeticOperations):
    def __init__(self, num1 = 0, num2 = 0):
        super().__init__(num1, num2)

    def accept_values(self):
        self.value1 = float(input("Enter first number: "))
        self.value2 = float(input("Enter second number: "))
        return self.value1, self.value2

a_obj1 = Arithmetic()
a_obj1.accept_values()

ret_addition = a_obj1.addition()
print("Addition is: ",ret_addition)

ret_substraction = a_obj1.substraction()
print("Substraction is: ",ret_substraction)

ret_multiplication = a_obj1.multiplication()
print("Multiplication is: ",ret_multiplication)

ret_division = a_obj1.division()
print("Division is: ",ret_division)
