list1 = []
list2 = []
for _ in range(3):
    a = list(map(int,input().split()))
    list1.append(a)
input()
for _ in range(3):
    a = list(map(int,input().split()))
    list2.append(a)
for i in range(3):
    for j in range(3):
        print(list1[i][j] * list2[i][j], end = ' ' )

    

    print()