print("Hello, World!")
print('This is a test of the Python basics exercise.')
print()
name = input("What is your name? \n")
print(f"Hello, {name}! Welcome to the Python basics exercise.")

# This is a comment explaining that the following code will ask for the user's age and print a message based on their input.
age = int(input("How old are you? \n"))
if age < 18:
    print("You are a minor.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

first_name = input("What is your first name? \n")
last_name = input("What is your last name? \n")
print(f"Your full name is {first_name.capitalize()} {last_name.capitalize()}.")

print('Hello, {} {}'.format(first_name.capitalize(), last_name.capitalize()))
print('Hello, {0} {1}'.format(first_name.capitalize(), last_name.capitalize()))
print(f"Hello, {first_name.capitalize()} {last_name.capitalize()}")

