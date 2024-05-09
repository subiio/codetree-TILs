N = int(input())
list_info = [
    list(map(int, input().split()))
    for _ in range(N)
]
max_sum =0
for i in range(N):
    for j in range(N-2):
    

        s =0
        s = list_info[i][j] + list_info[i][j+1] + list_info[i][j+2]
        max_sum = max(max_sum,s)

print(max_sum)