try:
    # this is a read file
    with open("tests.txt", "r") as f:
        content = f.read()
        print(content)

except FileNotFoundError as e:
    print("File not found error:", e)

#finally vanthu error vanthulum work agun
finally:
    print("close the connection,clean up resources")