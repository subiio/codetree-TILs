n = int(input())

class People:
    def __init__(self,name,bungi,area):
        self.name =name
        self.bungi = bungi
        self.area = area




list1 = []
min_inx = 0
for _ in range(n):
    name,bungi,area = tuple(input().split())
    list1.append(People(name,bungi,area))

for i in range(n):
    if list1[min_inx].name > list1[i].name:
        min_inx = i

print(f"name {list1[min_inx].name}")
print(f"addr {list1[min_inx].address}")
print(f"city {list1[min_inx].region}")