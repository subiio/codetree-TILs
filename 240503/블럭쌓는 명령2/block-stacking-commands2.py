N,K = map(int,input().split())

list2 = [0]*N 
list1 = []
for _ in range(K):
    list1.append(tuple(map(int,input().split())))

for i in range(len(list1)):
    for j in range(list1[i][0],list1[i][1]+1):
        list2[j] += 1
print(max(list2))