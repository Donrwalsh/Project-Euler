'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

x = 1
sum = 0
sieve = [False] * 2000000
sieve[1] = True
for i in range(2, 2000000):
    if sieve[i] == False:
        sum += i
        n = i
        while n < 2000000:
            sieve[n] = True
            n += i

print(sum)