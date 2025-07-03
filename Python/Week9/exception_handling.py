#exception handling
'''
try:
    print(x)
except NameError:
    print("variable x is not defined")
except:
    print("Something went wrong")
finally:
    print("try except is finished")
'''
'''
# Example of exception handling in Python
try:
    print(x)
except NameError:
    print("variable x is not defined")
else:
    print("try except is finished")
'''


# Example of raising an exception with a custom message
x = -1
if x < 0:
    raise Exception("x cannot be negative")
