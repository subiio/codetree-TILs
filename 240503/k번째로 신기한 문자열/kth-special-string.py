n,k,T =input().split()
n = int(n)
k = int(k)
list1 = []

for _ in range(n):
    a = input()
    count = 0
    if len(a) < len(T):
        pass
    else:
        for i in range(len(T)):
            if a[i] == T[i] :
                count += 1
                if count == len(T):
                    list1.append(a)

print(sorted(list1)[k-1])