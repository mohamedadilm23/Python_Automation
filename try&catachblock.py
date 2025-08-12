try:
    with open("wrote.txt" "r") as error:
        error.read()

except:
 print("some how i reached  block because there is failure in try block")

 try:
     with open("wrote.txt" "r") as error1:
      error1.read()

 except Exception as e:
     print(e)

finally:
    print("cleaning the process")

