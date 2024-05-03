n,k,T =input().split()
n = int(n)
k = int(k)
list1 = []
for _ in range(n):
    list1.append(input().split())
list2 = sorted(list1)
print(list2[k][0])