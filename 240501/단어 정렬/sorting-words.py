n = int(input())

list1 = []
for _ in range(n):
    list1.append(input())

a = sorted(list1)

for i in a:
    print(i)