class Calculator:
    def add(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        return a + b

    def subtract(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        return a - b

    def multiply(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        result = 0
        if b < 0 and a < 0:
            b = abs(b)
            a = abs(a)
            for i in range(b):
                result = self.add(result, a)
            return result
        elif b < 0 and a > 0:
            b = abs(b)
            a = abs(a)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        elif b > 0 and a < 0:
            b = abs(b)
            a = abs(a)
            result = 0
            for i in range(b):
                result = self.add(result, a)
            return -result
        else:
            for i in range(b):
                result = self.add(result, a)
            return result

    def divide(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        assert b != 0, "Cannot divide by zero"
        if (a < 0 or b < 0) and abs(a) > abs(b):
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = abs(self.subtract(a, b))
                result += 1
            return result
        elif (a < 0 and b < 0) or (a > 0 and b > 0):
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return result
        else:
            a = abs(a)
            b = abs(b)
            result = 0
            while a >= b:
                a = self.subtract(a, b)
                result += 1
            return -result
    
    def modulo(self, a, b):
        assert isinstance(a, int) and isinstance(b, int), "Arguments must be integers"
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(8,4))
    print("Example: modulo: ", calc.modulo(10, 3))