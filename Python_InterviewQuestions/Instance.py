class MyClass:


    1



class MyClass:
    @classmethod
    def class_method(cls):
        return "Class"

    def instance_method(self):
        return "Instance"


# Create an object (instance)
obj = MyClass()

# Call instance method
print(obj.instance_method())   # Instance

# Call class method
print(MyClass.class_method())  # Class



"""  Rule of thumb:

Use instance methods when you need data from that particular object.

Use class methods when you need to work with the class itself, not individual objects.

"""

