from collections import deque
import copy

n, k = map(int,input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

r,c = map(int,input().split())

q = deque()

pyeongga_list = [[0 for _ in range(n)] for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]

answer= [[0 for _ in range(n)] for _ in range(n)]

order = 1

def in_range(x,y):
    return (0<= x < n) and (0<= y < n)


def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == True or pyeongga_list[x][y] == 0:
        return False
    return True

def push(x,y):
    visited[x][y] = True
    q.append((x,y))

prev_x, prev_y = r-1, c-1

max_x , max_y =  101 ,101 
max_number = 0



def bfs():
    global max_number, max_x, max_y
    while q:
        dxs, dys = [1,0,-1,0], [0,1,0,-1]
        curr_x , curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x,new_y):
                # print("cango: ", new_x, new_y)
                if max_number < grid[new_x][new_y]:
                    max_x = new_x
                    max_y = new_y
                    max_number = grid[new_x][new_y]
                elif max_number == grid[new_x][new_y]:
                    if new_x < max_x:
                        max_x = new_x
                        max_y = new_y
                        max_number = grid[new_x][new_y] 
                    elif new_x == max_x:
                        if new_y < max_y:
                            max_x = new_x
                            max_y = new_y
                            max_number = grid[new_x][new_y]


                push(new_x, new_y)

for i in range(k):
    number = grid[prev_x][prev_y]
    pyeongga_list = copy.deepcopy(grid)

    for j in range(n):
        for k in range(n):
            if grid[j][k] >= number and (j != prev_x or k != prev_y):
                pyeongga_list[j][k] = 0
    # print(pyeongga_list)
    push(prev_x,prev_y)
    bfs()

    prev_x, prev_y = max_x, max_y
    max_x, max_y = 101, 101
    max_number = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
if n == 1:
    print(1,1)
else:
    print(prev_x+1, prev_y+1)