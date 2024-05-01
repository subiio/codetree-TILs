n,m = map(int,input().split())
list1 = []
list2 = []
for _ in range(n):
    a = list(map(int,input().split()))
    list1.append(a)
for _ in range(n):
    a = list(map(int,input().split()))
    list2.append(a)

for i in range(n):
    for j in range(m):
        print( 0 if list1[i][j] == list2[i][j] else 1, end = ' ' )
    print()