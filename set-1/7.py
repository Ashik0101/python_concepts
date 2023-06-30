# check if a given number is prime number

def check_prime(num):
    factors = 0
    for i in range(num):
        if num % (i+1) == 0:
            factors += 1
    return factors <= 2


print(check_prime(14))
print(check_prime(143))
print(check_prime(19))
print(check_prime(7))
