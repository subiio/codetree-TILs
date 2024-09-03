n,m = map(int,input().split())


grid =  []
for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = []
for i in range(n):
    add = []
    for j in range(m):
        add.append(False)
    visited.append(add)

order = 1

def in_range(x,y,n,m):
    return (0 <= x < n) and (0 <= y < m )

def can_go(x,y):
    if not in_range(x,y,n,m):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    return True
def dfs(x,y):
    global order
    dxs, dys = [1,0], [0,1]
    for dx, dy in zip(dxs, dys):
        new_x = x + dx
        new_y = y + dy

        if can_go(new_x,new_y) :
            grid[new_x][new_y] = order
            order += 1
            visited[new_x][new_y] = 1
            dfs(new_x,new_y)
    
    if grid[n-1][m-1] <= 1:
        return 0
    else:
        return 1

grid[0][0] = order
visited[0][0] = 1
dfs(0,0)
# if grid[n-1][m-1] <= 1 :
#     print(0)
# else:
#     print(1)