n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))


visited = [[False for _  in range(n)] for _ in range(n)]

count = 0 
result = []

def in_range(i,j):
    return 0 <= i < n and 0 <= j < n


def available(i,j):

    # dxs, dys = [1,0,-1,0], [0,1,0,-1]
    if not in_range(i,j):
        return False
    if (visited[i][j] == True) or (grid[i][j] == 0):
        return False

    # for dx, dy in zip(dxs,dys):
    #     new_ix = i + dx 
    #     new_iy = j + dy

    #     if (grid[i+dx][j+dy] == 0) or (visited[i+dx][j+dy] == True):
    #         return False
    
    return True


def dfs(x,y):
    global grid, count , result

    dxs,dys = [1,0,-1,0], [0,1,0,-1]

    for dx, dy in zip(dxs,dys):
        new_x = x + dx
        new_y = y + dy
        if available(new_x,new_y):
            # print("1 new_x, new_y: ", new_x, new_y)
            count += 1
            visited[new_x][new_y] = True
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if available(i,j):

            visited[i][j] = True
            count = 1

            dfs(i,j)

            result.append(count)


result.sort()

print(len(result))

for i in range(len(result)):
    print(result[i])