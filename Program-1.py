class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str):
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example
calc = Calculator(10, 5)
print(calc.calculate("add"))       # 15
print(calc.calculate("divide"))    # 2.0
