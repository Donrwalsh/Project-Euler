'''
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


from datetime import datetime
start=datetime.now()

def isprime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

x = 5
sum = 5
track = 2000
while x < 2000000:
    if isprime(x):
        sum += x
    x += 2
    if x > track:
        print (str((track/2000)*.1) + "% complete " + str(datetime.now()-start))
        track += 2000
print(sum)

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