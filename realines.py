
file = open("write.txt")  # Open the file named 'write.txt' in read mode by default
for i in file.readlines(): # Loop through all lines using readlines()
 print(i) # Print each line
file.close() # Always close the file after use