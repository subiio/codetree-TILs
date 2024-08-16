n = int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

r,c,m1,m2,m3,m4,dir = map(int,input().split())

r -=1
c -=1 
grid_list = []
center = [r,c]
grid_list.append(grid[r][c])
for i in range(1,m1+1):
    array = [-1, 1]
    grid_list.append(grid[r+array[0]*i][c+array[1]*i])
    center = [r+array[0]*i, c+array[1]*i]
r2,c2 = center[0],center[1]
for j in range(1,m2+1):
    array = [-1,-1]
    grid_list.append(grid[r2+array[0]*j][c2+array[1]*j])
    center = [r2+array[0]*j, c2+array[1]*j]
r3,c3 = center[0], center[1]
for k in range(1,m3 +1):
    array = [1, -1]
    # print(r3+ array[0]*k, c3+ array[1]*k)
    grid_list.append(grid[r3 + array[0]*k][c3+array[1]*k])
    center = [r3+array[0]*k, c3+array[1]*k]
r4,c4 = center[0], center[1]
for l in range(1,m4):
    array = [1,1]
    grid_list.append(grid[r4 + array[0]*l][c4 + array[1]*l])
    center = [r4+array[0]*l, c4+array[1]*l]

# print("r,c:",r,c,"r2,c2:",r2,c2,"r3,c3: ",r3,c3,"r4,c4: ",r4,c4)
# print(grid_list)


if dir == 0:
    length =0
    for i in range(1,m1+1):
        array = [-1 ,1]
        grid[r+array[0]*i][c+array[1]*i] = grid_list[length]
        length += 1
    for j in range(1,m2+1):
        array = [-1, -1]
        grid[r2+array[0]*j][c2 + array[1]*j] = grid_list[length]
        length += 1
    for k in range(1,m3+1):
        array = [1, -1]
        grid[r3+array[0]*k][c3 + array[1]*k] = grid_list[length]
        length += 1
    for l in range(1,m4 + 1):
        array = [1,1]
        grid[r4+ array[0]*l][c4 + array[1]*l] =grid_list[length]
        length += 1
    
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end= " ")
        print()
else:
    length = 1
    stop_flag = 0

    for i in range(0,m1+1):
        array = [-1, 1]
        grid[r+array[0]*i][c+array[1]*i] = grid_list[length]
        length += 1
    for j in range(1,m2+1):
        array = [-1, -1]
        grid[r2+array[0]*j][c2 + array[1]*j] = grid_list[length]
        length += 1
    for k in range(1,m3+1):
        if length > len(grid_list)-1:
            length = -1
            stop_flag = 1
        array = [1, -1]
        grid[r3+array[0]*k][c3 + array[1]*k] = grid_list[length]
        length += 1
        if stop_flag == 1:
            break
    for l in range(1,m4 + 1):
        if stop_flag == 1:
            break
        array = [1,1]
        if length > len(grid_list)-1:
            length = -1
            stop_flag = 1
        grid[r4+ array[0]*l][c4 + array[1]*l] =grid_list[length]
        length += 1
    for i in range(n):
        for j in range(n):
            print(grid[i][j], end= " ")
        print()