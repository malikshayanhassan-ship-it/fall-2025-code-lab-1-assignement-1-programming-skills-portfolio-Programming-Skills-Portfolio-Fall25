#Basic Quiz Program
# Ask the question
answer = input("What is the capital of France? ")

# Check the answer
if answer == "Paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The correct answer is Paris.")



# Improved Quiz Program
# Asking the question
answer = input("What is the capital of France? ")

# Convert input to lowercase for comparison
if answer.lower() == "paris":
    print("Correct! The capital of France is Paris.")
else:
    print("Wrong! The correct answer is Paris.")


#Advanced Quiz Program with Multiple Questions
# Dictionary of countries and their capitals
quiz = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Switzerland": "Bern",
    "Belgium": "Brussels",
    "Austria": "Vienna",
    "Denmark": "Copenhagen"
}

score = 0  # keeping track of correct answers

print("Welcome to the European Capitals Quiz!\n")

# Looping through each country and asking the user
for country, capital in quiz.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f" Wrong! The correct answer is {capital}.\n")

# Final score
print(f"Your final score: {score}/{len(quiz)}")
