N = input()
N = int(N)

list1 = list(map(int,input().split()))

max_list = max(list1)
count = 0
list2 = []
for i in list1:
    count += 1
    list2.append(i)
    if max_list == i:
        break

max_list2 = max(list2)
count2 = 0
for j in list2:
    count2 += 1
    if max_list2 == i:
        break
print(count,count2)