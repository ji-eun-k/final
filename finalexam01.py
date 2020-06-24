import math


def pipi(i):
    sum = 0.0
    for j in range(1, i, 1):
        sum = sum + (-1) ** (j + 1) / (2 * j - 1)
    return sum

print("{:4}     {:4}".format('i', 'mi(i)'))
for i in range(2,1002,100) :
    sum = pipi(i)
    print("{:4}     {:.4F}".format(i-1, 4 * sum))