n = int(input())

class Score:
    def __init__(self,name,kor,eng,math):
        self.name = name
        self.kor = kor
        self.eng =eng
        self.math =math

people=[]
for _ in range(n):
    name,kor,eng,math = tuple(input().split())
    people.append(Score(name,kor,eng,math))

people.sort(key= lambda x: (-int(x.kor),-int(x.eng),-int(x.math)))

for i in range(n):
    print(people[i].name,people[i].kor,people[i].eng,people[i].math)