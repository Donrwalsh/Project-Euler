'''
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def isprime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

n = 1
i = 1
while n < 10002:
    if isprime(i):
        print(str(n) + ": " + str(i))
        n += 1
    i += 1