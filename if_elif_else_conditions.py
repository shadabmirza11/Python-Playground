# Taking user input
number = int(input("Enter your number: "))

# Check if the number is positive
if number > 0:
    print(f"{number} is positive.")
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
# Check if the number is negative
elif number < 0:
    print(f"{number} is negative.")
    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")
# If the number is zero
else:
    print("The number is zero.")