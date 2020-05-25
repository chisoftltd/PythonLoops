# Program by ChisoftMedia
import math
import random as rd
import numpy as np


from filecmp import cmp

a = 456
b = 100
c = 0b100

d = a/b

print(c)


# Convertion from decimal to binary
x = 200
y = 47

z_bin = bin(x)

print(z_bin)

print(bin(y))


# Convertion from binary to decimal
i = 0b01010
j = 0b0101110
k = i/j


print(i)

print(k)

print(float(i))

print(complex(k))

print(complex(i, k))


# Mathematical Functions

print(abs(complex(i, k)))

print(math.ceil(k))

print(math.exp(k))


del k


k = i >> 3


print(k)

print(i >> 2)

print((math.floor(d)))

print(math.pow(a, d))

del a, b, c

# Random Number Function


a = rd.randrange(0, 11, 1)
print(a)


a = np.arange(0, 110, 1)
print(a)

# Trig Functions

x = 0.64

print(math.acos(x))

print(math.atan(x))

print(math.cos(x))

print(math.radians(x))