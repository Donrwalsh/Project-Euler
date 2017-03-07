'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math

def isprime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

def check_divis(x, list):
    for item in list:
        if x % item == 0:
            return False
    return True

result = []
i = 3
big_num = 600851475143
while i < math.sqrt(big_num):
    if big_num % i == 0:
        if check_divis(i, result):
            if isprime(i):
                result.append(i)
                print ("Found " + str(i))
    i += 1

print("Largest Prime Factor found to be " + str(max(result)))