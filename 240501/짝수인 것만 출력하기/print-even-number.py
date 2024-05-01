n = input()
n = int(n)
list2 = []
list1 = list(map(int,input().split()))

for i in list1:
    if i%2 == 0:
        list2.append(i)
    else:
        pass

for j in list2:
    print(j, end = ' ')