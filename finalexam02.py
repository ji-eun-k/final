import math


class Point:
    x = 0
    y = 0

    def __init__(self, i, j):
        self.x = i
        self.y = j

    def __add__(self,other):
        print('두 점의 위치 더하기 : ({}, {})'.format(self.x + other.x,self.y + other.y))

    def distance(self,other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


p1 = Point(1, 1)
p2 = Point(2, 2)
print("distance : {}".format(p1.distance(p2)))
p1 + p2

