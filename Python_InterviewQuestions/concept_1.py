#What is the difference between a list and a tuple?
#list are mutable ,tuples are Immutable

#list are modified
#tuples are not modified

my_list=[1,2,3,4]

my_list[0]=100

#add one more values
my_list.append(2000)

#remove the index index 3is---->4 show removed output(100,2,3,2000)
my_list.pop(3)

print(my_list)

#tuples--tuple' object does not support item assignment
my_tuple=(1,2,3,4,)

#my_tuple[0]=500

print(my_tuple)

#----------------------------------------------------------------------------------#

#2. what are datatypes in python
#what is dictionary
#dictionary is collection of key and values pair


x=10 #int
y= 3.14 #float
#very importnat topic dictionary
d={"a":1}
s="hello"
z=True #boolean

#----------------------------------------------------------------------------------#
