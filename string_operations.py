# 1.Checking for vowels in a string
s = "shadab"
vowels1 = "aeiouAEIOU"
# Iterate over each character in string s
for i in s:
    if i in vowels1:
        print(i)
        
# 2.Count the number of vowels in another string
t = "Mirza"
vowels2 = "aeiouAEIOU"
count = 0
# Iterate over each character in string t and count vowels
for i in t:
    if i in vowels2:
        count += 1
print(count)

# 3.Capitalizing the first letter of the string
a = "apple is a fruit."
print(a.capitalize())

# 4.Converting the string to lowercase
b = "Banana is my favorite fruit."
print(b.lower())

# 5.Converting the string to uppercase
c = "Banana is my favorite fruit."
print(c.upper())

# 6.Removing leading and trailing spaces from the string
d = "Today is Saturday."
print(d.strip())

# 7.Splitting the string by a space
e = "All is well."
print(e.split(" "))  
