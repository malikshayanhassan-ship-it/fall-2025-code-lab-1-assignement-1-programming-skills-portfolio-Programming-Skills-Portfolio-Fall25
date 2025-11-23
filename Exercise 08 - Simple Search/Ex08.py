#Basic
def main():
    # The list of names as defined in the requirements
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    search_term = "Sam"
    
    print(f"Searching for '{search_term}' in the list...")
    
    # Simple flag to track if we found it
    found = False
    
    for name in names:
        if name == search_term:
            found = True
            break  # Stop looking once we find it
            
    if found:
        print(f"Success! {search_term} is in the list.")
    else:
        print(f"{search_term} was not found.")

if __name__ == "__main__":
    main()

#Advanced
def main():
    names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
    
    # Ask the user what to look for
    search_term = input("Enter the name you want to search for: ")
    
    # This variable tracks the result
    found = False
    
    # Loop through each name to check against the input
    for name in names:
        # Case-insensitive check (optional but good for user input)
        if name.lower() == search_term.lower():
            found = True
            break
            
    if found:
        print(f"Yes, {search_term} is in the list.")
    else:
        print(f"Sorry, {search_term} is not in the list.")

if __name__ == "__main__":
    main()