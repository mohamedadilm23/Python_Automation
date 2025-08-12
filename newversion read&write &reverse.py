#read the file and store all the lines in list
#reverse list
#write the list back to the file
from os import write

#file open and close
with open("write.txt","r") as readfile:
    #list of values
  cointains = readfile.readlines()

 #list of values as reverse
reversed(cointains)

#file open and close
with open("write.txt","w") as writer:
    for i in reversed(cointains):
        writer.write(i)

#reversed words
#goo
#bye
#Good
#How are u
#Hi welcome to VDart Group