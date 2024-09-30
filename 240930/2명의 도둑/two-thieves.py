N,M,C = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

# # N,M,C = 4, 3, 12
# # # grid = [[8,8,6,5],[5,2,7,4],[8,5,1,7],[1,1,1,1]]
# N,M,C = 5,2, 16
# grid = [[8,6,2,6,8],[3,8,4,3,5],[8,1,9,1,2],[6,7,3,9,4],[9,7,1,2,6]]
# N,M,C = 5,5,26
# grid = [[6, 9, 5, 5, 2], 
# [4, 4, 7, 8, 1],
# [7, 4, 2, 9, 3], 
# [7, 7, 8, 6, 8], 
# [4, 6 ,5 ,8 ,2 ]]
# 8 6 2 6 8 
# 3 8 4 3 5 
# 8 1 9 1 2 
# 6 7 3 9 4 
# 9 7 1 2 6 


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

# def count_backtracking(cur_num,grid,empty_list= []):
#     if cur_num == len(grid):
#         return
#     if empty_list is not None:
#         for k in (empty_list):
#             subset = k
#             for i in range(cur_num, len(grid)):
#                 empty_list.append(grid[i])
#                 count_backtracking(cur_num + 1,grid,)
#     else:
#         for j in range(len(grid)):
#             empty_list.append(grid[i])
#             count_backtracking(cur_num + 1,grid,empty_list)



def generate_subsets(arr, C):
    result = []
    max_square_sum = 0

    def backtrack(start, subset):
        nonlocal max_square_sum
        subset_sum = sum(subset)

        # 부분 리스트의 합이 C를 넘지 않는 경우에만 제곱의 합을 계산
        if subset_sum <= C:
            square_sum = sum([x**2 for x in subset])
            # 최대 제곱 합을 갱신
            max_square_sum = max(max_square_sum, square_sum)

        # start부터 arr의 각 원소를 추가하거나 추가하지 않음
        for i in range(start, len(arr)):
            # 원소를 부분리스트에 추가
            subset.append(arr[i])
            # 다음 재귀 호출에서 선택할 원소들을 결정
            backtrack(i + 1, subset)
            # 마지막 원소 제거 (다른 조합을 탐색하기 위해)
            subset.pop()

    backtrack(0, [])
    return max_square_sum
    

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
        max_number1 = generate_subsets(grid3_grid,C)
        


            

        # for i in range(1,len(grid3_grid)):
        #      for k in range(len(grid3_grid)):
        #         grid1 = []
        #         sum_number = 0
        #         for l in range(i):
        #             # print(i,k,l)
        #             grid1.append(grid3_grid[(k+l)%len(grid3_grid)])
        #             sum_number += (grid3_grid[(k+l)%len(grid3_grid)]) **2
                
        #         if sum(grid1) <= C:
        #             print("grid3:", grid1)
        #             max_number1 = max(sum_number,max_number1)
        #             print("max_number1: ", max_number1)
        #         else:
        #             pass 

    if sum_number_2 <= C:
        for n in grid4_grid:
            max_number2 += n*n 
    else:
        max_number2 = generate_subsets(grid4_grid,C)
        # for i in range(1,len(grid4_grid)):
        #      for k in range(len(grid4_grid)):
        #         grid2 = []
        #         sum_number = 0
        #         for l in range(i):
        #             # print(k+l)
        #             grid2.append(grid4_grid[(k+l) % len(grid4_grid)])
        #             sum_number += (grid4_grid[(k+l) % len(grid4_grid)]) **2
        #         # print("grid2: ", grid2)
        #         if sum(grid2) <= C:
        #             print("grid4: ", grid2)
        #             max_number2 = max(sum_number,max_number2)
        #             print("max_number2: ", max_number2)
        #         else:
        #             pass 
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