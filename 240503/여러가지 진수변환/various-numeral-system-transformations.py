N,B = map(int,input().split())
list1 = []
while True:
    if N < B:
        list1.append(N)
        break
    
    list1.append(N%B)
    
    N //= B


for list2 in list1[::-1]:
    print(list2, end ='')