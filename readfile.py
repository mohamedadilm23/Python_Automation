file = open('write.txt')        # Step 1: Open the file for reading

print(file.read(5))             # Step 2: Read the first 5 characters
print(file.read())              # Step 3: Read the rest of the file
print(file.read())              # Step 4: Try to read again



#print line by line using readline method:
line=file.readline()
#while using a loop checking a condition blank
while line!="":
 print(line)
line=file.readline()
file.close()   # Step 5: Close the file
