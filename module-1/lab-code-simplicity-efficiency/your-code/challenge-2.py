import string 
import random

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

def RandomStringGenerator(l=12, a=(list(string.ascii_lowercase) + list(str(i) for i in range(0,10)))):
    p = 0
    s = ''
    while p<l:
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(int(n)):
        if int(a) < int(b):
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            raise Exception("Incorrect min and max string lengths. Try again.")
        r.append(RandomStringGenerator(c))
    return r
​
print(BatchStringGenerator(int(n), int(a), int(b)))