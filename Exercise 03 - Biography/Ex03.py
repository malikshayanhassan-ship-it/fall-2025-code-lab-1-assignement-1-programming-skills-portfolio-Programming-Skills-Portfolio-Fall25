# Get user input
name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
age_input = input("Enter your age: ")

# Check if age is a number
if age_input.isdigit():
    age = int(age_input)
else:
    print("Invalid input for age. Setting age to 0.")
    age = 0  # default value if input is not a number

# Store the data in a dictionary
bio = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines
print("\nYour Biography:")
print(bio["name"], bio["hometown"], bio["age"], sep="\n")
