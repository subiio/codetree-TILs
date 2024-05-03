N =int(input())


class Point:
    def __init__(self,x,y,number):
        self.x = x
        self.y = y
        self.number= number

point = [
]

for i in range(1,N+1):
    x,y = tuple(input().split())
    point.append(Point(x,y,i))

point.sort(key = lambda x: ((abs(0-int(x.x))) + abs(0-int(x.y))))


for i in range(N):
    print(point[i].number)