from parent import Calculator
class Child(Calculator):
    #create one variable
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 100, 200)

#create one method
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


light = Child() #Current class calling
print(light.getCompleteData())
