new = 10

# A while loop keeps running as long as the condition is True
while new > 1:
    # if new != 5:   # Skip printing 5

    if new==4:
        new = new - 1
        continue

    if new == 2:  # ✅ When new becomes 2, break the loop
        break
    print(new)    # ✅ Print current value of new

    # Decrease value of new
    new = new - 1  # ✅ Subtract 1 from new in each loop



#new = new - 1
#✅ Step 1: new = 10
#10 > 1 → True → print(10)
#new = 9

#✅ Step 2: new = 9
#9 > 1 → True → print(9)
#new = new - 1
#new = 8

#✅ Step 3: new = 8
#8 > 1 → True → print(8)
#new = new - 1
#new = 7

#new=7
#7>1-> True->print(7)
#new = new - 1
#new=6

#new=6
#7>1-> True->print(6)
#new = new - 1
#new=5

#✅ Step 4: new = 5
#5 > 1 → True → skip print because 5 == 5
#new = new - 1
#new = 4

#✅ Step 5: new = 4
#4 > 1 → True → print(4)
#new = new - 1
#new = 3

#✅ Step 6: new = 2
#2 > 1 → True → print(2)
#new = new - 1
#new = 1

#❌ Step 7: new = 1
#1 > 1 → False → loop exits
