import math


def pipi(i):
    sum = 0.0
    for j in range(1, i, 1):
        sum = sum + (-1) ** (j + 1) / (2 * j - 1)
    print("{:4}     {:.4F}".format(i, 4 * sum))

print("{:4}     {:4}".format('i', 'mi(i)'))
for i in range(2,902,100) :
    pipi(i)