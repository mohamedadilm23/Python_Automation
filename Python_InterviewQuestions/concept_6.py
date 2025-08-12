#How do you sorting a list

numbers=[8,9,4,5,7,2,1,3]

#how to reverse to sorted lst
print(numbers[::-1])

#sorted list
print(sorted(numbers))

#---------------------------------------------------------------------------------#

""" Python's Default Behavior: Synchronous Execution
Python executes code line by line in a blocking manner.
Each operation must complete before the next one starts.
● This is how Python normally works unless explicitly told to run asynchronously
Python Supports Asynchronous Execution Using asyncio
Python can run non-blocking tasks using asyncio.
Instead of waiting for one task to finish, multiple tasks run concurrently."""