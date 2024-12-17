# Function to return product if <= 1000, otherwise sum
def multiplication_and_sum(number1, number2):
    product = number1 * number2
    if product <= 1000:
        return product
    else:
        return number1 + number2

# Given test cases
result1 = multiplication_and_sum(20, 30)  # Product is 600 (less than 1000)
print(result1)

result2 = multiplication_and_sum(40, 30)  # Product is 1200 (greater than 1000, so sum)
print(result2)
