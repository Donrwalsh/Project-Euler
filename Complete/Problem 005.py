'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''


def test(x):
    for i in range(11, 21): #1-10 are covered by 11-20, no need to double check.
        if x % i != 0:
            return False
    return True

x = 1
result = 0
while result == 0:
    if test(x):
        result = x
    else:
        x += 1

print(result)