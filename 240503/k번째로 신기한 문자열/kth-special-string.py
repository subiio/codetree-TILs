n,k,T =input().split()
n = int(n)
k = int(k)
list1 = []
for _ in range(n):
    list1.append(input())

print(sorted(list1)[k])