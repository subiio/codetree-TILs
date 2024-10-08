N,M,Q = map(int,input().split())
grid= []
for _ in range(N):
    grid.append(list(map(int,input().split())))

moving = []
for _ in range(Q):
    moving.append(list(map(str,input().split())))

def toggle(d):
    if d == "L":
        d = "R"
    else:
        d = "L"
    return d

def rotation(grid,r,d,M):
    if d == "L":
        temp = grid[r-1][M-1]
        for i in range(M-1,0,-1):
            grid[r-1][i] = grid[r-1][i-1]
        
        grid[r-1][0] = temp
    else:
        temp = grid[r-1][0]
        for i in range(1,M):
            grid[r-1][i-1] = grid[r-1][i]
        grid[r-1][M-1] = temp
    return grid

for i in moving:
    first_moving_direction = i[1]
    if N == 1 and M == 1:
        break
    elif N == 1:
        grid = rotation(grid,int(i[0]),i[1],M)
    else:
        temp = first_moving_direction
        grid = rotation(grid,int(i[0]),temp,M)
        for j in range(int(i[0])-1, 0, -1):
            temp = toggle(temp)
            for k in range(M):
                if (grid[j-1][k] == grid[j][k]):
                    grid = rotation(grid,j,temp,M)

                    break
                
        temp2 = first_moving_direction
        for l in range(int(i[0]), N):
            # print("l: ", l)
            # print(l)
            temp2 = toggle(temp2)
            # print("i[1]:", i[1])
            for m in range(M):
                # print("m: ",m)
                if (grid[l][m] == grid[l-1][m]):
                    grid = rotation(grid,l+1,temp2,M)

                    break
if N == 1 and M == 1  :
    print(grid[0][0])
else:
    for i in range(N):
        for j in range(M):
            print(grid[i][j], end = " ")
        print()