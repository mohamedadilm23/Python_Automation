#how do you read and write files in python

#this is a write a file
with open("test.txt","w") as f:
    f.write("Hello world Mohamed adil")


#this is a read a file

with open ("test.txt","r") as f:
 content=f.read()
 print(content)


 #==============================================================#
 #what are  fixture in  pytest? when they are used?

 import pytest


 @pytest.fixture
 def sample_data():
     print("\nSetup: Creating test data")  # Runs before the test
     data = {"name": "Alice", "age": 30}
     return data  # Provides data to the test


 def test_example(sample_data):
     assert sample_data["name"] == "Alice"
     assert sample_data["age"] == 30
     print("Test executed successfully")



#---------------------------------------------------------#
#How to do you use yield for WebDriver Setup
#and Teardown in pytest

 @pytest.fixture
 def sabaya():
     print("\nSetup: Creating test data")  # Runs before the test
     data = {"name": "Alice", "age": 30}
     #
     yield data  # Provides data to the test
     print("cleaning the process")


 def test_sam(sabaya):
     assert sabaya["name"] == "Alice"
     assert sabaya["age"] == 30
     print("Test executed successfully")

     
