N = int(input())
coins = []

for _ in range(N):
    coins.append(list(map(int,input().split())))

max_coin = 0
for i in range(N):
    for j in range(N):
        if i+2 >= N or j+2 >= N:
            continue
        tmp = 0
        for k in range(i, i+3):
            for l in range(j, j+3):
                if coins[k][l] == 1:
                    tmp += 1
        if tmp >= max_coin:
            max_coin = tmp

print(max_coin)