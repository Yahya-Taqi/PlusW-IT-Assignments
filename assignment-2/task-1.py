## Reading user name
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ");

## Changing the capitalization
firstName = firstName.upper()
lastName = lastName.upper()

## Calculating the Length of the name
nameLength = len(firstName) + len(lastName)

## Printing
print(f"First Name: {firstName}")
print(f"Last Name: {lastName}")
print(f"Number of characters in your name: {nameLength}")