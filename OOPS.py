class Fan:
    piece = 100

 #default constructor
    def __init__(self):
        print("Hi I am created automatically object is created")

    def getdata(self):
        print("Hello fan how are u")

obj=Fan() #syntax to create objects in python
obj.getdata()
print(obj.piece)