def main():
    CORRECT_PASSWORD = "12345"
    access_granted = False

    print("---PASSWORD CHECK ---")
    
    # Keep asking until the correct password is provided
    while not access_granted:
        user_input = input("Enter password: ")

        if user_input == CORRECT_PASSWORD:
            access_granted = True
            print("Access Granted!")
        else:
            print("Incorrect. Please try again.")

if __name__ == "__main__":
    main()

#advanced version 
def main():
    CORRECT_PASSWORD = "12345"
    MAX_ATTEMPTS = 5
    attempts_count = 0
    
    print(f"--- SECURE SYSTEM ({MAX_ATTEMPTS} attempts max) ---")

    while attempts_count < MAX_ATTEMPTS:
        user_input = input("\nEnter password: ")

        if user_input == CORRECT_PASSWORD:
            print("\n>> ACCESS GRANTED.")
            print(">> Welcome to the system.")
            return # Exit the function immediately on success
        else:
            attempts_count += 1
            remaining = MAX_ATTEMPTS - attempts_count
            
            if remaining > 0:
                print(f"Incorrect password. {remaining} attempt(s) remaining.")
            else:
                print("\n>> aCCESS DENIED.")
                print(">> maximum attempts reached.")
                print("!!! aUTHORITIES HAVE BEEN ALERTED !!!")

if __name__ == "__main__":
    main()