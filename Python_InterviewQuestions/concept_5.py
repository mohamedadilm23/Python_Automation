#how do you create list of dictnaries
#

#list of dictonaries like json foemat
data=[{"name":"bob", "age":21, "gender":"male"}, #0 index
      {"name":"Adil", "age":24, "gender":"male"}, #1 index
      {"name": "John", "age": 29, "gender": "male"}] #2index


#we have access the file
print(data[1])
print(data[2]["age"])

#------------------------------------------------------#
#.what is lambda in python ? and how its is applied between map(),filter() functions

"""1.A lambda function in Python is a small, anonymous function
that can have multiple arguments but only one expreſsion.
2.It is written in a single line.
3.It is used where a short function is needed temporarily.
Don't use lambda if the function is complex-use def instead
"""

#normal method or function
a=10
b=20
def add (a,b):
    return a+b
print(add(a,b))

#easy method using lambda function
sub=lambda a,b :a-b
print(sub(a,b))

#map
"""In Python, map() is a built-in function that applies another function
 to each item in an iterable (like a list, tuple, etc.) and 
 returns a map object (which is an iterator).
 "map() na oru helper, unga function ah each element ku apply pannum."
"""
#map is a elemninating list it does not have condition to apply
num=[1,2,3,4,5,6,7,8,9,10]
square=map(lambda a:a*2,num)
print(list(square))


#filter
evennumbers=list(filter(lambda a: a%2==0,num))
print(evennumbers)

""" 💡 Difference from map():

map() → transforms each item.

filter() → removes items that don’t match the condition."""

