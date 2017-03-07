'''
Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

for a in range(0, 1001):
    for b in range(0, 1001-a):
        for c in range(1000-a-b, 1001-a-b):
            if (a*a + b*b == c*c) and a < b < c:
                print(str(a) + ", " + str(b) + ", " + str(c))
                print(str(a * b * c))