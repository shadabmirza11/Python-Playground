# Take string from the user
str_input = input("Please, enter a word: ")

# Get the length of the string
p = len(str_input)

# Loop through the string to display characters at even index numbers
for i in range(0, p, 2):
    print(f"Character at index {i}: {str_input[i]}")
