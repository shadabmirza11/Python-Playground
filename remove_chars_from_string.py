# Function to remove characters from a string from 0 to n and return a new string
def remove_chars(word, n):
    # Slice the string starting from index n to the end
    new_word = word[n:]
    return new_word

# Test cases
result1 = remove_chars("Python", 4)
print(result1)  # Output: tive

result2 = remove_chars("Python", 2)
print(result2)  # Output: native