n,t = map(int,input().split())

grid = []

for _ in range(3):
    grid.append(list(map(int,input().split())))



def rotation(grid,n):
    temp1= grid[0][n-1]
    temp2 = grid[1][n-1]
    temp3 = grid[2][n-1]
    for i in range(3):
        for j in range(n-1,0,-1):
            grid[i][j] = grid[i][j-1] 

    grid[0][0] = temp3
    grid[1][0] = temp1
    grid[2][0] = temp2

    return grid


for _ in range(t):
    grid = rotation(grid,n)


for i in range(3):
    for j in range(n):
        print(grid[i][j], end= " ")
    print()