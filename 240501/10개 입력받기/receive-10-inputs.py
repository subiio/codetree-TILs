list1 = list(map(int,input().split()))
index = 0
list2 = []
for i in list1:
    if i == 0:
        break
    index += 1

for i in range(0,index):
    list2.append(list1[i])

print(sum(list2), "%.1f" %(sum(list2)/len(list2)))