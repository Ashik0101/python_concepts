# calculate factorial of number
def calculate_factorial(num):
    sum = 1
    for i in range(num):
        sum *= (i+1)
    return sum


print("Factorial of 5 is: ", calculate_factorial(5))
