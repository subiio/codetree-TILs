n = int(input())

a = list(map(int,input().split()))
answer = 100000
for i in range(n):
    S = 0
    for j in range(n):
        S += a[j]*(abs(i-j))
        
    answer = min(S,answer)

print(answer)