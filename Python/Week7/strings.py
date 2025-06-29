#strings
#use triple quotes to create a multi-line string.
''''message = """Bob's world
is cool
like python"""
print(message)
'''
# string indexing
''''message = "Randy"
print(message[0])  # First character)
print(message[1])  # Second character
print(message[2])  # Third character

#string slicing
print(message[0:3])  # First three characters
print(message[1:])   # From second character to the end
print(message[-1])   # Last character
'''

# string methods
message = "Randy is cool"
print(message.upper())  # Convert to uppercase
print(message.lower())  # Convert to lowercase
print(message.title())  # Convert to title case
print(message.capitalize())  # Capitalize the first letter
print(message.replace("cool", "awesome"))  # Replace a substring
print(message.split(' '))  # Split the string into a list of words after each space
print(message.find("is"))  # Find the index of a substring
print(message.count("o"))  # Count occurrences of a character
print(message.startswith("Randy"))  # Check if the string starts with a substring
print(message.endswith("cool"))  # Check if the string ends with a substring
print(len(message))  # Get the length of the string)
# String concatenation
greeting = "Hello"
name = "Randy"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)
