'''Write a code to return True if the list’s first and last numbers are the same. 
If the numbers are different, return False.

Given:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]'''
#Answer:
def numbers_n(numberlist):
    firstnum = numberlist[0]
    secondnum = numberlist[-1]
    if firstnum == secondnum:
        return True
    else:
        return False
numbers_x= [10, 20, 30, 40, 10]
print(numbers_n(numbers_x))
numbers_y = [75, 65, 35, 75, 30]
print(numbers_n(numbers_y))

    