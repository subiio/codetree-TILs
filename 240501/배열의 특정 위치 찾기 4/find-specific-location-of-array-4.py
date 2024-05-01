list1 = list(map(int,input().split()))
index = 0
list2 = []
for i in range(len(list1)):
    if list1[i] == 0:
        break
    index += 1
for j in range(0,index):
    list2.append(list1[j])

count = 0
sum1 = 0
for i in list2:
    if i%2 == 0:
        count += 1
        sum1 += i
    else:
        pass

print(count,sum1)