from collections import deque
import copy

n, k = map(int, input().split())

# 그리드 입력
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 시작 위치 입력 (0-index로 변환)
r, c = map(int, input().split())
prev_x, prev_y = r - 1, c - 1

# BFS 사용을 위한 설정
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]

# 상하좌우 이동을 위한 델타
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# 범위 확인 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 이동 가능 여부 확인 함수
def can_go(x, y, number):
    return in_range(x, y) and not visited[x][y] and grid[x][y] < number

# BFS 함수
def bfs(x, y):
    global max_x, max_y, max_number
    q.append((x, y))
    visited[x][y] = True
    number = grid[x][y]

    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x, new_y, number):
                if grid[new_x][new_y] > max_number:
                    max_x, max_y = new_x, new_y
                    max_number = grid[new_x][new_y]
                elif grid[new_x][new_y] == max_number:
                    if new_x < max_x or (new_x == max_x and new_y < max_y):
                        max_x, max_y = new_x, new_y
                visited[new_x][new_y] = True
                q.append((new_x, new_y))

# k번 이동하는 과정
for _ in range(k):
    max_x, max_y = prev_x, prev_y
    max_number = -1
    visited = [[False for _ in range(n)] for _ in range(n)]
    bfs(prev_x, prev_y)

    # 이동할 수 없으면 중단
    if (max_x, max_y) == (prev_x, prev_y):
        break

    prev_x, prev_y = max_x, max_y

# 최종 위치 출력 (1-index로 변환)
print(prev_x + 1, prev_y + 1)