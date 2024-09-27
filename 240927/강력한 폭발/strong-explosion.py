import copy

n = int(input())

# 입력받은 격자판을 저장
original_grid = []
for _ in range(n):
    original_grid.append(list(map(int, input().split())))

# 폭탄이 놓여야 할 위치를 저장
explode_list = []
for i in range(n):
    for j in range(n):
        if original_grid[i][j] == 1:
            explode_list.append([i, j])

# 폭발 패턴에 따른 좌표 이동 값
dx = [[0, 1, 2, -1, -2], [0, 0, 0, 1, -1], [0, -1, 1, 1, -1]]
dy = [[0, 0, 0, 0, 0], [0, 1, -1, 0, 0], [0, 1, -1, 1, -1]]

max_num = 0

# 백트래킹 함수
def backtracking(curr_num, grid):
    global max_num
    if curr_num == len(explode_list):
        # 초토화된 영역의 수 계산
        count = sum([sum(row) for row in grid])
        max_num = max(max_num, count)
        return

    # 현재 폭탄을 놓을 위치
    cur_x, cur_y = explode_list[curr_num]

    # 폭발 패턴 적용
    for k in range(len(dx)):
        temp_grid = copy.deepcopy(grid)  # 폭발 후 상태 저장을 위해 깊은 복사
        for l in range(5):
            nx = cur_x + dx[k][l]
            ny = cur_y + dy[k][l]
            if 0 <= nx < n and 0 <= ny < n:
                temp_grid[nx][ny] = 1  # 해당 위치를 폭발시킴

        # 다음 폭탄을 놓는 백트래킹 단계로 넘어감
        backtracking(curr_num + 1, temp_grid)

# 백트래킹 시작
backtracking(0, copy.deepcopy(original_grid))
print(max_num)