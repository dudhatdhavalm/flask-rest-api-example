class Calculator1:
    def summation(self, a, b):
        return a + b


class Calculator2:
    def devide(self, a, b):
        return a / b


class Calculator(Calculator1, Calculator2):
    __count = 0

    def multi(self, a, b):
        print("Count => " + str(self.__count + 1))
        return a * b

    def methodName(cls):
        print(cls)
        cls.__count = 25
        print(cls.__count)


animal = Calculator()
print(isinstance(animal, Calculator))
print(issubclass(Calculator1, Calculator))
print(animal.summation(10, 20))
print(animal.devide(10, 20))
print(animal.multi(10, 20))
animal.methodName()
