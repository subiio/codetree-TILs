list1 = []
for _ in range(2):
    a = list(map(int,input().split()))
    list1.append(a)

list2 = []
list3 = []

sum1 = 0
total= 0

for i in range(2):
    list2.append(sum(list1[i])/len(list1[i]))
for j in range(4):
    list3.append((list1[0][j] + list1[1][j])/2)
for i in range(2):
    for j in range(4):
        sum1 += list1[i][j]

total = sum1/8

for i in list2:
    print("%.1f" %(i), end =' ')
print()    
for j in list3:
    print("%.1f" %(j), end = ' ')
print()
print("%.1f" %(total))