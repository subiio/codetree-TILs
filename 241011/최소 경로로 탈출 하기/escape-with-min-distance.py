from collections import deque
n,m = map(int,input().split())

grid = []

q = deque()

for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = [[False for _ in range(m)] for _ in range(n)]

step = [[0 for _ in range(m)] for _ in range(n)]
def in_range(x,y):
    return (0 <= x < n) and (0 <= y < m)

def can_go(x,y):
    if not in_range(x,y):
        return False

    if grid[x][y] == 0 or visited[x][y] == True:
        return False
    return True


def push(x,y,s):
    visited[x][y] = True
    q.append((x,y))
    step[x][y] = s


def bfs():
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    while q:
        curr_x, curr_y = q.popleft()
        for dx,dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx , curr_y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y,step[curr_x][curr_y]+1)

push(0,0,0)
bfs()
print(step[n-1][m-1])