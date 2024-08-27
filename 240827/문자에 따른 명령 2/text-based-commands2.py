dir_num = 3
# 북쪽
dx,dy= [1,0,-1,0], [0,-1,0,1]

a = input()
rotation = list(a)

grid = [0,0]
for i in range(len(rotation)):
    if rotation[i] == "L":
        dir_num = (dir_num -1 + 4) % 4
    elif rotation[i] == "R":
        dir_num = (dir_num + 1) % 4
    else:
        grid[0] = grid[0] + dx[dir_num]
        grid[1] = grid[1] + dy[dir_num]

for i in range(len(grid)):
    print(grid[i], end =" ")