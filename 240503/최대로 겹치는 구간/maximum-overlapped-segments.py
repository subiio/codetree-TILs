n = int(input())

list1 = [0] *400
list2 = []
for i in range(n):
    list2.append(list(map(int,input().split())))

for i in range(len(list2)):
    for j in range(list2[i][0],list2[i][1]-1):
        list1[j] += 1

print(max(list1))