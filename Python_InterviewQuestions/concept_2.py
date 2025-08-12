# 3. How do you implement inhertiance and super keyword in python

#what is inhertiance ?
# A inhertitance is acquiring properites of childclass to parentclass

#1.Methods, 2.attributes,from another class
#example


#2. super keyword using parentclass accessing
#parent class

class Parent:
    def apple(self):
        return "Hello from parent"

class Child(Parent):
    def pineapple(self):
        parent_message = super().apple()
        return f"{parent_message} and hello from child"

c = Child()  # ✅ create an instance

print(c.pineapple())  # Child method using super()
print(c.apple())      # Parent method



#---------------------------------------------------------------------#
#super keyword is parent accesing
#fan is a class
class Home:
    def fan(self):
        return "Fan is ON while current is coming"

class TopHome(Home):
    def fan(self):
        # Call parent method using super()
        parent_message = super().fan()
        return f"{parent_message} | Fan is OFF while current is cut"

# Create an object
f = TopHome()

# Call method
print(f.fan())

""" 
self is not a keyword but a convention in Python.
It refers to the current instance of a class.
It must be the first parameter in instance method Python
though you don't need to pass it explicitly when calling methods. Console
Unlike some languages (like Java or C++), Python does not have an explicit this keyword. Instec
self is used to access instance variables and methods inside the class"""
