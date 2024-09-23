n = int(input())
# [0] 남 [1] 동 [2] 서 [3] 북
dx = [1,0,-1,0]
dy = [0,1,0,-1]

grid = []


for i in range(n):
    grid.append(list(map(int,input().split())))

# n = 3
# grid = [[1,2,1],[4,5,6],[1,8,1]]

def in_range(x,y):
    return (0<= x < n and 0 <= y < n)

def explode(grid,i,j):
    # 폭발의 크기
    n = grid[i][j]
    explode_grid = [[i,j]]
    if n == 1:
        pass
    else:
        for k in range(1,n):
            for l in range(len(dx)):
                explode_grid.append([i + k*dx[l],j + k*dy[l]])
    # print(explode_grid)
    for o in explode_grid:
        if in_range(o[0],o[1]):
            grid[o[0]][o[1]] = 0
        else:
            pass
    # print(grid)
    return grid

def gravity(grid,i,j):
    global n
    N = i
    if i == 0:
        return grid
    else:
        for k in range(n):
            N = i
            # print(k,N)
            if grid[N][k] == 0:
                while N !=0:
                    # print("N: ", N-1)
                    # print("grid[N][j]", grid[N][k])
                    # print("grid[N-1][j]", grid[N-1][k])
                    grid[N][k] = grid[N-1][k]
                    N -= 1
                grid[N][k] = 0
        # print("gravited:", grid)
        return grid


### 여기가 fucking 문제야
def calculate(grid):
    count = 0
    for u in range(n):
        for y in range(n):
            if grid[u][y] >= 1:
                for b in range(len(dx)):
                    dxs = u
                    dys = y
                    dxs += dx[b]
                    dys += dy[b]
                    if in_range(dxs,dys):
                        if grid[u][y] == grid[dxs][dys]:
                            count += 1
                        else:
                            pass
                    else:
                        pass
    # print(count/2)
    return int(count/2)





num_list = []

if n== 1:
    print(0)
else:
    
    for i in range(n):
        for j in range(n):
            exploded_grid = grid
            exploded_grid = explode(grid,i,j)
            gravitied_grid = gravity(exploded_grid,i,j)
            num_list.append(calculate(gravitied_grid))

    print(max(num_list))