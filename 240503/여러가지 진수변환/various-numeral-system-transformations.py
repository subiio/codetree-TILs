N,B = map(int,input().split())
list1 = []
while True:
    if N < 4:
        list1.append(N)
        break
    
    list1.append(N%B)
    
    N //= B

print(*list1[::-1],sep = '')