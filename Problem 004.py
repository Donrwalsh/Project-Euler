'''
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
result = 0

for i in range(101, 1000):
    for j in range(101, 1000):
        dat_string = str(i*j)
        gnirts_tad = dat_string[::-1]
        if dat_string == gnirts_tad and i*j > result:
            result = i*j
print(result)