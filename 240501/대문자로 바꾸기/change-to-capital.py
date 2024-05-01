list1 = []
for _ in range(5):
    a = list(map(str,input().split()))
    list1.append(a)

for i in range(5):
    for j in range(3):
        list1[i][j] = chr(ord(list1[i][j]) + (ord('A')-ord('a')))
        print(list1[i][j],end = ' ')
    print()