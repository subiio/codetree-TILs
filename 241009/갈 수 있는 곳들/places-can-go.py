from collections import deque



n,k = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]
start_point = []


for _ in range(k):
    start_point.append(list(map(int,input().split())))


def in_range(x,y):
    return (0<= x < n) and (0 <= y < n)

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == True or grid[x][y] == 1:
        return False
    return True
def push(x,y):
    visited[x][y] = True
    q.append((x,y))


q = deque()
def bfs():
    while q:
        dxs, dys = [1,0,-1,0], [0,1,0,-1]
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y)


for i in start_point:
    push(i[0]-1, i[1]-1)
    bfs()

# print(visited)

count = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == True:
            count += 1
print(count)