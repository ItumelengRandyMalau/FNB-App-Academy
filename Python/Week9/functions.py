#writing functions
'''
def greet(name):
    """This function greets the person passed in as a parameter."""
    print(f"Hello, {name}!")
greet("Lwandle")

#function to add two numbers and return the result
def add(a, b):
    return a + b
print(add(5, 3))
'''

def greet(name, message="Hello"):
    """This function greets the person passed in as a parameter with a custom message."""
    print(f"{message} {name}!")
greet("Lwandle", "Good day")