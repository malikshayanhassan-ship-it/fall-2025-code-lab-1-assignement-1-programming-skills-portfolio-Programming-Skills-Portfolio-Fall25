# This program runs through several counting tasks using for loops
# Each section prints the numbers as requested

print("--- Task 1: Count up from 0 to 50 ---")
# range(51) goes from 0 up to (but not including) 51
for i in range(51):
    print(i)

print("\n--- Task 2: Count down from 50 to 0 ---")
# To include 0, we set the stop value to -1
for i in range(50, -1, -1):
    print(i)

print("\n--- Task 3: Count up from 30 to 50 ---")
for i in range(30, 51):
    print(i)

print("\n--- Task 4: Count down from 50 to 10 (steps of 2) ---")
# We stop at 9 to ensure 10 is the last number printed
for i in range(50, 9, -2):
    print(i)

print("\n--- Task 5: Count up from 100 to 200 (steps of 5) ---")
# We stop at 201 to ensure 200 is included
for i in range(100, 201, 5):
    print(i)