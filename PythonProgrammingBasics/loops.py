# FOR loops
fruits = ["apple", "orange", "pear", "cherry", "grapes", "banana"]

for fruit in fruits:
    print("Would you like {}?".format(fruit))
    
for number in range(1,11):
    print("Number {}".format(number))
    
# WHILE loops
temp_f = 40

"""while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1"""
    
# LOOP CONTROLS
"""
    Break: end the look, go to the next statement in the program (outside the loop)
    Continue: skips current part of the loop, moves to the next part of the loop
    Pass: skips any part of the loop where "pass" appears, best used for testing code
"""

while temp_f > 32:
    print("The water is {} degrees".format(temp_f))
    temp_f -= 1
    
    if temp_f == 33:
        break
    
for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("This is the number {}".format(number))