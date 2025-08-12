# self is a class instance we have access everywhere in the class

# constructor
# What is init() in Python?
# The __init__() method is known as a constructor in object-oriented programming (OOP)
# terminology. It is used to initialize an object's state when it is created. This method is
# automatically called when a new instance of a class is instantiated.


class Parent:

    def apple(self):
        return "Hello from parent"
    

# parent message="Hello from parent"

class Child(Parent):

    # paramatrize constructor
    def __init__(self, title):
        # entha title self.title object la stored pani classes access panvom
        self.title = title

    def pineapple(self):
        parent_message = super().apple()
        return f"{parent_message} and hello from child" + self.title


c = Child("Hello self I have created new")  # ✅ create an instance

print(c.pineapple())  # Child method using super()
print(c.apple())  # Parent method

# output is
# Hello from parent and hello from child Hello self I have created new
# Hello from parent
