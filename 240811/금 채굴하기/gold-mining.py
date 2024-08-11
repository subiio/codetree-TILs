n, m = map(int, input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 누적 합 배열 계산
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = (grid[i - 1][j - 1] + 
                            prefix_sum[i - 1][j] + 
                            prefix_sum[i][j - 1] - 
                            prefix_sum[i - 1][j - 1])

def get_sum(x1, y1, x2, y2):
    return (prefix_sum[x2 + 1][y2 + 1] - 
            prefix_sum[x1][y2 + 1] - 
            prefix_sum[x2 + 1][y1] + 
            prefix_sum[x1][y1])

max_gold = 0

for k in range(n):
    cost = k * k + (k + 1) * (k + 1)
    for i in range(n):
        for j in range(n):
            left = max(0, j - k)
            right = min(n - 1, j + k)
            up = max(0, i - k)
            down = min(n - 1, i + k)
            tmp = get_sum(up, left, down, right)
            if tmp * m >= cost and tmp > max_gold:
                max_gold = tmp

print(max_gold)