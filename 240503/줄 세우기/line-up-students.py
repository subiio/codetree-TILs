N = int(input())

class body:
    def __init__(self,height,weight,number=1):
        self.height = height
        self.weight = weight
        self.number = number

people = []

for i in range(1,N+1):
    height,weight = tuple(input().split())
    people.append(body(height,weight,i))

people.sort(key = lambda x: (-int(x.height),-int(x.weight),-int(x.number)))

for j in range(N):
    print(people[j].height,people[j].weight,people[j].number)