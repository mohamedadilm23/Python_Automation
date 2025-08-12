#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different purpose
#constructor name should be __init__
#new keyword is not required when you create object

class Calculator:
    num = 100  #class variables
    #default constructor

    def __init__(self, a, b): #constructor
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

    def flower(self):
        print("Flowervalues")
        return self.firstNumber + self.secondNumber


light = Calculator(2, 3)
light.getData()
print(light.Summation())

light1 = Calculator(4, 5)
light1.getData()
print(light1.Summation())

light2= Calculator(1,3)
light2.getData()
print(light2.flower())





