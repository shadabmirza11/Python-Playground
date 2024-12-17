# Continuously take input from the user
while True:
    # Taking input from user as integer
    number = int(input("Enter a number: "))

    # If the number is even, skip it using continue
    if number % 2 == 0:
        print(f"{number} is even, skipping it.")
        continue
    
    # If the number is greater than 5, stop the loop using break
    if number > 10:
        print(f"Stopping the loop, {number} is greater than 10.")
        break
    
    # If the number is odd and not greater than 5, print it
    print(f"Number is odd and not greater than 10: {number}")
