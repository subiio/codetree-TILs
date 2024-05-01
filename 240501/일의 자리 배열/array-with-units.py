list1 = list(map(int,input().split()))

for i in range(2,10):
    list1.append((list1[i-1]+list1[i-2])%10)

for j in list1:
    print(j,end=' ')