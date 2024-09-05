n = int(input())
grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))


def count_number_1(grid):
    count = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                count += 1
    return count
max_count = 0
bomb_list = [[0 for _ in range(n)]
for _ in range(n)]
bombed = [
    [0 for _ in range(n)]
    for _ in range(n)
]
explode_pose = []
explode_list = [[[-2,0],[-1,0],[0,0],[1,0],[2,0]],
    [[-1,0],[1,0],[0,0],[0,1],[0,-1]],
    [[-1,-1],[-1,1],[0,0],[1,1],[1,-1]]]
def find_max_explode(curr_num):
    global max_count, grid, explode_list
    # print("curr_num: ", curr_num)
    # print("explode_pose_list: ", explode_pose_list)
    if curr_num == len(explode_pose) :
        for i in range(n):
            for j in range(n):
                bombed[i][j] = False
        
        for i in range(n):
            for j in range(n):
                if bomb_list[i][j]:
                    for k in range(5):
                        dx, dy = explode_list[bomb_list[i][j]][k]
                        nx, ny = i + dx, j + dy
                        try:
                            bombed[nx][ny] = 1
                        except:
                            pass       
        tmp = count_number_1(bombed)

        if tmp > max_count:
            max_count = tmp

        return
    explode_list = [[[-2,0],[-1,0],[0,0],[1,0],[2,0]],
        [[-1,0],[1,0],[0,0],[0,1],[0,-1]],
        [[-1,-1],[-1,1],[0,0],[1,1],[1,-1]]]
    for k in range(len(explode_list)):
        point_explode = explode_pose[curr_num]
        bomb_list[point_explode[0]][point_explode[1]] = k 
        find_max_explode(curr_num + 1)
        bomb_list[point_explode[0]][point_explode[1]] = 0
   
    
    return

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            explode_pose.append([i,j])
prev_grid = 0
find_max_explode(0)
print(max_count)