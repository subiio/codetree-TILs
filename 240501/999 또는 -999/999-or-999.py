list1 = list(map(int,input().split()))
list2 = []
for i in list1:
    if i == 999 or i == -999:
        break
    else:
        list2.append(i)

tmp1 = list1[0]
tmp2 = list1[0]
for j in list2:
    if j > tmp1:
        tmp1 = j
    if j < tmp2:
        tmp2 = j

print(tmp1,tmp2)