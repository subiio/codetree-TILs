n = int(input())

list1 = list(map(int,input().split()))
list2 = []
for i in range(n):
    for j in range(i+1,n):
        list2.append(abs(list1[i]-list1[j]))

print(min(list2))