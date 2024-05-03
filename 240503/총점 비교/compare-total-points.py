n = int(input())
class Score:
    def __init__(self,name,a,b,c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
    
people= []
for _ in range(n):
    name,a,b,c = tuple(input().split())
    people.append(Score(name,a,b,c))

people.sort(key= lambda x : int(x.a) + int(x.b) + int(x.c))

for i in range(n):
    print(people[i].name,people[i].a,people[i].b,people[i].c)