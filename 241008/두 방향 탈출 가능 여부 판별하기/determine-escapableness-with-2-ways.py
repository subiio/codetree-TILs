n,m = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))


visited = [[False for _ in range(m)] for _ in range(n)]

def in_range(i,j):
    global n,m 
    return (0 <= i < n) and (0 <= j < m)


def cango(i,j):
    if not in_range(i,j):
        return False
    elif visited[i][j] == True or grid[i][j] == 0:
        return False

    return True

count = 0
def dfs(x,y):

    global grid, count

    dxs , dys = [1,0], [0, 1]
    for dx, dy in zip(dxs, dys):
        new_x , new_y = x + dx , y + dy
        
        if cango(new_x,new_y):
            # print("x,y: ", new_x, new_y)
            if new_x == n-1 and new_y == m-1:
                count += 1
            visited[new_x][new_y] = True
            dfs(new_x,new_y)

dfs(0,0)
print(count)