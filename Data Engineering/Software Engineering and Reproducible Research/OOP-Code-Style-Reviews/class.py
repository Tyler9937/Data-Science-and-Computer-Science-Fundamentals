# Document experimenting with a simple class
class Complex:
    def __init__(self, initial):
        self.initial = initial

    def add(self, added):
        return self.initial + added

    def subtract(self, subtracted):
        return self.initial - subtracted

    def multiply(self, multiplied):
        return self.initial * multiplied

    def divide(self, divided):
        return self.initial / divided


x = Complex(3.0)
print(x.add(4.0))
print(x.subtract(5.0))
print(x.multiply(5.0))
print(x.divide(3.0))
