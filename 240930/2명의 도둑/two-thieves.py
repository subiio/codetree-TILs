N,M,C = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

# N,M,C = 4, 3, 12



bubun_list =[]

for i in range(N):
    for j in range(N-M+1):
        bubun_list_2 = []
        for m in range(j,j+M):
            bubun_list_2.append([i,m])
        bubun_list.append(bubun_list_2)

# print(bubun_list)

def check_possible(grid1,grid2):
    for i in grid1:
        if i in grid2:
            return False
    return True

doduk_grid =[]
max_num = 0

def find_max_num(grid3,grid4,C,global_grid):
    
    sum_number = 0
    sum_number_2 = 0
    grid3_grid = []
    grid4_grid = []
    max_number1 = 0
    max_number2 = 0
    max_number = 0
    for i in range(len(grid3)):
        # print(grid[0][0])
        sum_number +=  global_grid[grid3[i][0]][grid3[i][1]] 
        grid3_grid.append(global_grid[grid3[i][0]][grid3[i][1]])
        sum_number_2 += global_grid[grid4[i][0]][grid4[i][1]]
        grid4_grid.append(global_grid[grid4[i][0]][grid4[i][1]])
    # print("grid3_grid4:", grid3_grid, grid4_grid)
    if sum_number<= C:
        for n in grid3_grid:
            max_number1 += n*n 
    else:
        for i in range(1,len(grid3_grid)):
             for k in range(len(grid3_grid)):
                grid1 = []
                sum_number = 0
                for l in range(i):
                    # print(i,k,l)
                    grid1.append(grid3_grid[(k+l)%len(grid3_grid)])
                    sum_number += (grid3_grid[(k+l)%len(grid3_grid)]) **2
                # print(grid)
                if sum(grid1) <= C:
                    # print("grid3:", grid)
                    max_number1 = max(sum_number,max_number1)
                    # print("max_number1: ", max_number1)
                else:
                    pass 

    if sum_number_2 <= C:
        for n in grid4_grid:
            max_number2 += n*n 
    else:
        for i in range(1,len(grid4_grid)):
             for k in range(len(grid4_grid)-(i-1)):
                grid2 = []
                sum_number = 0
                for l in range(i):
                    grid2.append(grid4_grid[(k+l) % len(grid4_grid)])
                    sum_number += (grid4_grid[(k+l) % len(grid4_grid)]) **2
                if sum(grid2) <= C:
                    # print("grid4: ", grid2)
                    max_number2 = max(sum_number,max_number2)
                    # print("max_number2: ", max_number2)
                else:
                    pass 
    temp = max_number1 + max_number2
    max_number = max(temp, max_number)
    # print(max_number)
    
    return max_number

maxing_number = 0
def backtracking(curr_num,idx):
    global maxing_number
    if curr_num == 2:
        if check_possible(doduk_grid[0],doduk_grid[1]):
            temp = find_max_num(doduk_grid[0],doduk_grid[1],C,grid)
            maxing_number = max(temp,maxing_number)
        else:
            pass
    
    for i in range(idx,len(bubun_list)):
        doduk_grid.append(bubun_list[i])
        backtracking(curr_num + 1, idx + 1)
        doduk_grid.pop()

backtracking(0,0)

print(maxing_number)