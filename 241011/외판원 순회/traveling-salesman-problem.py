n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

visited = [False for _ in range(n)]  # n 크기의 방문 여부 리스트
min_cost = float('inf')

def backtracking(curr_num, current_cost, start_node, path_len):
    global min_cost

    # 모든 도시를 방문한 후 다시 시작점으로 돌아옴
    if path_len == n and grid[curr_num][start_node] > 0:
        min_cost = min(min_cost, current_cost + grid[curr_num][start_node])
        return

    for next_node in range(n):
        if not visited[next_node] and grid[curr_num][next_node] > 0:
            visited[next_node] = True
            backtracking(next_node, current_cost + grid[curr_num][next_node], start_node, path_len + 1)
            visited[next_node] = False

# 1번 노드를 시작점으로 설정
visited[0] = True
backtracking(0, 0, 0, 1)

print(min_cost)