'''
#for loop

import numbers


fruits = ["Banana", "Apple", "Cherry"]
for fruit in fruits:
    print(fruit)

numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)
'''
'''
#While loop

count = 0

while count <= 7:
    print(count)
    count += 1  # Increment count by 1 each iteration
'''

#loop control statements

#break statement
fruits = ["Banana", "Apple", "Cherry"]
for fruit in fruits:
    if fruit == "Apple":
        break  # Exit the loop when "Apple" is found
    print(fruit)

print()

#continue statement
fruits = ["Banana", "Apple", "Cherry"]
for fruit in fruits:
    if fruit == "Apple":
        continue  # Skip the rest of the loop when "Apple" is found and moves in to the next iterarion
    print(fruit)

#pass statement
print()

fruits = ["Banana", "Apple", "Cherry"]
for fruit in fruits:
    if fruit == "Apple":
        pass  # Do nothing when "Apple" is found, just continue the loop
    print(fruit)