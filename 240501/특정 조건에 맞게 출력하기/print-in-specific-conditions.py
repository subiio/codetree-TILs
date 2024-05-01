list1 = list(map(int,input().split()))
list2= []
for i in list1:
    if i == 0:
        break
    else:
        list2.append(i)
list3 = []

for j in list2:
    if j%2 == 0:
        print(j//2, end = ' ')
    else:
        print(j+3,end = ' ')