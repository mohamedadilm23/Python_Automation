
value=[1,20,30,40,"sahil"]
# list is datatype that allows multiple values and can be diffrent data types
print(value[0],value[2],value[4]) #1 30 sahil

print(value[-2])  #40                        ast index -2 reduce
print(value[1:4]) # [20, 30, 40]                  1-4 index printed

value.insert( 5 ,"ahmed")
print(value) #1, 20, 30, 40, 'sahil', 'ahmed']

value.append("trichy")
print(value) #[1, 20, 30, 40, 'sahil', 'ahmed', 'trichy']

 #updating
value[4]="SAHIL" #[1, 20, 30, 40, 'SAHIL', 'ahmed', 'trichy']
print(value)

#DEL Values
del value [2]
print(value) #[1, 20, 40, 'SAHIL', 'ahmed', 'trichy']




