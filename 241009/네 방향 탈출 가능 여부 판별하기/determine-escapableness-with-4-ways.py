from collections import deque

n,m = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

answer = [[0 for _ in range(m)] for _ in range(n)]

order = 1

goal_count = 0

visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()

def in_range(x,y):
    return (0 <= x < n) and (0 <= y < m)

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] == True or grid[x][y] == 0:
        return False
    return True


def push(x,y):
    global order
    answer[x][y] = order
    order += 1
    visited[x][y] = True
    q.append((x,y))
    





def bfs():
    global goal_count
    dxs = [1,0,-1,0]
    dys = [0,1,0,-1]

    while q:
        x,y = q.popleft()

        for dx, dy in zip(dxs,dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x,new_y):
                push(new_x, new_y)

push(0,0)
bfs()
if answer[n-1][m-1] == 0:
    print(0)
else:
    print(1)