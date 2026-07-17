from functools import reduce

factors_addition = lambda number1, number2: number1 + number2

class Numbers:
    def __init__(self, value = 0):
        value = int(input("Enter the number: "))
        self.num = value

    def ChkPrime(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num ** 0.5) + 1):
            if self.num % i == 0:
                return False
        return True

    def ChkPerfect(self):
        factors = []
        for i in range(1, self.num):
            if self.num % i == 0:
                factors.append(i)

        result = reduce(factors_addition, factors)
        return result == self.num

    def Factors(self):
        factors = []
        for i in range(1, self.num + 1):
            if self.num % i == 0:
                factors.append(i)
        
        return factors

class NumberOps(Numbers):
    def __init__(self, value = 0):
        super().__init__(value)

    def SumFactors(self):
        factors = self.Factors()
        return reduce(factors_addition, factors)
    
no_obj1 = NumberOps()
print("Is Prime Number: ", no_obj1.ChkPrime())
print("Is Perfect Number: ", no_obj1.ChkPerfect())
print("Factors of number are:", no_obj1.Factors())
print("Sum of Factors is: ", no_obj1.SumFactors())

print("-" * 70)

no_obj2 = NumberOps()
print("Is Prime Number: ", no_obj2.ChkPrime())
print("Is Perfect Number: ", no_obj2.ChkPerfect())
print("Factors of number are:", no_obj2.Factors())
print("Sum of Factors is: ", no_obj2.SumFactors())