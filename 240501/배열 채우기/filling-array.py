list1 = list(map(int,input().split()))
index = 0
list2 = []
if len(list1) > 10:
    print("False")
else:
    for i in list1:
        if i == 0:
            break
        index += 1
    for j in range(index-1,-1,-1):
        print(list1[j], end = ' ')