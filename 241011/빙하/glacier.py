from collections import deque
import copy


N,M = map(int,input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))


visited = [[False for _ in range(M)] for _ in range(N)]

q = deque()

def in_range(x,y):
    return (0 <= x < N) and (0 <= y < M)
def can_go(x,y):
    if not in_range(x,y):
        return False

    if grid[x][y] == 1 or visited[x][y] == True:
        return False
    
    return True
def push(x,y):
    visited[x][y] = True
    q.append((x,y))

def bfs():
    dxs,dys = [1,0,-1,0],[0,1,0,-1]

    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y)
iter_rate = True
time = 0

prev_count = 0
while iter_rate:
    count = 0
    prev_count = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    push(0,0)
    bfs()
    dxs,dys = [1,0,-1,0], [0,1,0,-1]

    for q in range(N):
        for w in range(M):
            if grid[q][w] == 0:
                prev_count += 1 
    for i in range(N):
        for j in range(M):
            
            if visited[i][j] == True:
                for dx, dy in zip(dxs, dys):
                    ind_x, ind_y = i + dx, j + dy
                    if in_range(ind_x, ind_y):
                        if grid[ind_x][ind_y]:
                            grid[ind_x][ind_y] = 0 

    for q in range(N):
        for w in range(M):
            if grid[q][w] == 0:
                count += 1 
    time += 1
    if count == N*M:
        iter_rate = False
        break

print(time, prev_count)