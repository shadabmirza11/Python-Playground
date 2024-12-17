# Given list of numbers
given = [10, 20, 33, 46, 55]

# Print the given list and a message
print(f"Given list is {given}\nDivisible by 5:")

# Iterate through the list to check divisibility by 5
for i in given:
    if i % 5 == 0:
        print(i)  # Print numbers divisible by 5