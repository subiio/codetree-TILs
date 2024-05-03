n,k,T =input().split()
n = int(n)
k = int(k)
list1 = []
for _ in range(n):
    a = input()
    if a[0] == 'a' and a[1] == 'p':
        list1.append(a)

print(sorted(list1)[k-1])