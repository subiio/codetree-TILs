N,M,C = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

bubun_list = []

for i in range(N):
    for j in range(N-M+1):
        bubun_list_2 = []
        for m in range(j, j+M):
            bubun_list_2.append([i, m])
        bubun_list.append(bubun_list_2)

def check_possible(grid1, grid2):
    for i in grid1:
        if i in grid2:
            return False
    return True

doduk_grid = []
max_num = 0

def find_max_sum_of_squares(subgrid, C, grid):
    """ 주어진 subgrid에서 C 이하의 합을 가지는 최대 제곱합을 찾는 함수 """
    n = len(subgrid)
    dp = [0] * (C+1)
    
    for i in range(n):
        value = grid[subgrid[i][0]][subgrid[i][1]]
        for j in range(C, value-1, -1):
            dp[j] = max(dp[j], dp[j-value] + value**2)
    
    return max(dp)

def find_max_num(grid3, grid4, C, global_grid):
    max_number1 = find_max_sum_of_squares(grid3, C, global_grid)
    max_number2 = find_max_sum_of_squares(grid4, C, global_grid)
    return max_number1 + max_number2

maxing_number = 0

def backtracking(curr_num, idx):
    global maxing_number
    if curr_num == 2:
        if check_possible(doduk_grid[0], doduk_grid[1]):
            temp = find_max_num(doduk_grid[0], doduk_grid[1], C, grid)
            maxing_number = max(temp, maxing_number)
        return
    
    for i in range(idx, len(bubun_list)):
        doduk_grid.append(bubun_list[i])
        backtracking(curr_num + 1, i + 1)
        doduk_grid.pop()

backtracking(0, 0)

print(maxing_number)