n = int(input())

list1 =[]
list2 = [0] * (1000) 
for _ in range(n):
    list1.append(list(map(int,input().split())))

for i in range(n):
    for j in range(list1[i][0],list1[i][1]+1):
        list2[j] += 1

print(max(list2))