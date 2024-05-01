n = int(input())
list1 = list(map(int,input().split()))

a = sorted(list1)
b = sorted(list1,reverse=True)

for i in a:
    print(i, end = ' ')
print()
for j in b:
    print(j, end = ' ')