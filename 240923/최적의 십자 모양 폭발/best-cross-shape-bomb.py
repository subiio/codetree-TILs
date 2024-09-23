import copy


n = int(input())
# [0] 남 [1] 동 [2] 서 [3] 북
dx = [1,0,-1,0]
dy = [0,1,0,-1]

grid = []


for i in range(n):
    grid.append(list(map(int,input().split())))

# n = 2
# grid = [[1,1],[1,2]]



def in_range(x,y):
    return (0<= x < n and 0 <= y < n)

def explode(grid_1,i,j):
    # 폭발의 크기
    F = grid_1[i][j]
    explode_grid = [[i,j]]
    if F == 1:
        pass
    else:
        for k in range(1,F):
            for l in range(len(dx)):
                explode_grid.append([i + k*dx[l],j + k*dy[l]])
    # print(explode_grid)
    for o in explode_grid:
        if in_range(o[0],o[1]):
            grid_1[o[0]][o[1]] = 0
        else:
            pass
    
    return grid_1

def gravity(grid_2,i,j,explode_range):
    global n
    N = i
    if i == 0:
        return grid_2
    else:
        for k in range(n):
            N = i
            # print(k,N)
            if grid_2[N][k] == 0 and k != j:
                while N !=0:
                    # print("N: ", N-1)
                    # print("grid[N][j]", grid[N][k])
                    # print("grid[N-1][j]", grid[N-1][k])
                    grid_2[N][k] = grid_2[N-1][k]
                    N -= 1
                grid_2[N][k] = 0
            elif grid_2[N][k] == 0 and k == j:
                grid_exploded = []
                try:
                    # print("N-explode_range + 1: ",)
                    for e in range(N, N - (explode_range - 1) -1 , -1):
                        grid_exploded.append(grid_2[e][k])
                    # print("grid_exploded: ", grid_exploded)
                    start_ind = 0
                    for z in range(N+(explode_range - 1), N-1, -1):
                        
                        grid_2[z][k] = grid_exploded[start_ind]
                        # print("start_ind: ", start_ind)
                        start_ind += 1

                except:
                    pass
                


        # print("gravited:", grid)
        return grid_2


### 여기가 fucking 문제야
def calculate(grid_3):
    count = 0
    for u in range(n):
        for y in range(n):
            if grid_3[u][y] >= 1:
                for b in range(len(dx)):
                    dxs = u
                    dys = y
                    dxs += dx[b]
                    dys += dy[b]
                    if in_range(dxs,dys):
                        if grid_3[u][y] == grid_3[dxs][dys]:
                            count += 1
                        else:
                            pass
                    else:
                        pass
    # print(count/2)
    return int(count//2)





num_list = []




for i in range(n):
    for j in range(n):
            grid_copy = copy.deepcopy(grid)
            # print("original_grid: ", grid_copy)
            exploded_grid = explode(grid_copy,i,j)
            # print("exploded_grid : ", exploded_grid)
            gravitied_grid = gravity(exploded_grid,i,j,grid_copy[i][j])
            # print("gravited_grid: " , gravitied_grid)
            num_list.append(calculate(gravitied_grid))

print(max(num_list))