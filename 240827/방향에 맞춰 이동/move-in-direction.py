n = int(input())
move_list = []

for _ in range(n):
    move_list.append(list(input().split()))

dx,dy = [1,0,-1,0], [0,-1,0,1]
grid = [0,0]
for i in range(len(move_list)):
    move_list[i][1] = int(move_list[i][1])
    if move_list[i][0] == "N":
        grid[0] = grid[0] + dx[3] * move_list[i][1] 
        grid[1] = grid[1] + dy[3] * move_list[i][1] 
    elif move_list[i][0] == "E":
        grid[0] = grid[0] + dx[0] * move_list[i][1] 
        grid[1] = grid[1] + dy[0] * move_list[i][1] 
    elif move_list[i][0] == "S":
        grid[0] = grid[0] + dx[1] * move_list[i][1] 
        grid[1] = grid[1] + dy[1] * move_list[i][1] 
    
    elif move_list[i][0] == "W":
        grid[0] = grid[0] + dx[2] * move_list[i][1] 
        grid[1] = grid[1] + dy[2] * move_list[i][1] 
    # print(grid)
for i in range(len(grid)):
    print(grid[i], end = " ")