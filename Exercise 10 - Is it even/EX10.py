def check_number(num):
    # Simple modulo check to see if it's divisible by 2
    if num % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."

def main():
    # Get input from the user
    user_input = input("Please enter a number: ")
    
    # Convert string input to an integer
    number = int(user_input)
    
    # Pass the number to our function and get the message back
    result_message = check_number(number)
    
    # Print the final result
    print(result_message)

if __name__ == "__main__":
    main()