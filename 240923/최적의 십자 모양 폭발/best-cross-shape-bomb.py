# import copy


# n = int(input())
# # [0] 남 [1] 동 [2] 서 [3] 북
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]

# grid = []


# for i in range(n):
#     grid.append(list(map(int,input().split())))

# # n = 2
# # grid = [[1,1],[1,2]]



# def in_range(x,y):
#     return (0<= x < n and 0 <= y < n)

# def explode(grid_1,i,j):
#     # 폭발의 크기
#     F = grid_1[i][j]
#     explode_grid = [[i,j]]
#     if F == 1:
#         pass
#     else:
#         for k in range(1,F):
#             for l in range(len(dx)):
#                 explode_grid.append([i + k*dx[l],j + k*dy[l]])
#     # print(explode_grid)
#     for o in explode_grid:
#         if in_range(o[0],o[1]):
#             grid_1[o[0]][o[1]] = 0
#         else:
#             pass
    
#     return grid_1

# def gravity(grid_2,i,j,explode_range):
#     global n
#     N = i
#     if i == 0:
#         return grid_2
#     else:
#         for k in range(n):
#             N = i
#             # print(k,N)
#             if grid_2[N][k] == 0 and k != j:
#                 while N !=0:
#                     # print("N: ", N-1)
#                     # print("grid[N][j]", grid[N][k])
#                     # print("grid[N-1][j]", grid[N-1][k])
#                     grid_2[N][k] = grid_2[N-1][k]
#                     N -= 1
#                 grid_2[N][k] = 0
#             elif grid_2[N][k] == 0 and k == j:
#                 grid_exploded = []
#                 for e in range(0,N-explode_range + 1):
#                     grid_exploded.append(grid_2[e][k])
#                 for z in range(N+(explode_range - 1), N-1, -1):
#                     grid_2[z][k] = grid_exploded.pop()
                


#         # print("gravited:", grid)
#         return grid_2


# ### 여기가 fucking 문제야
# def calculate(grid_3):
#     count = 0
#     for u in range(n):
#         for y in range(n):
#             if grid_3[u][y] >= 1:
#                 for b in range(len(dx)):
#                     dxs = u
#                     dys = y
#                     dxs += dx[b]
#                     dys += dy[b]
#                     if in_range(dxs,dys):
#                         if grid_3[u][y] == grid_3[dxs][dys]:
#                             count += 1
#                         else:
#                             pass
#                     else:
#                         pass
#     # print(count/2)
#     return int(count//2)





# num_list = []




# for i in range(n):
#     for j in range(n):
#             grid_copy = copy.deepcopy(grid)
#             # print("original_grid: ", grid_copy)
#             exploded_grid = explode(grid_copy,i,j)
#             # print("exploded_grid : ", exploded_grid)
#             gravitied_grid = gravity(exploded_grid,i,j,grid_copy[i][j])
#             num_list.append(calculate(gravitied_grid))

# print(max(num_list))

        
import copy

# 방향 설정: [남, 동, 서, 북]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def in_range(x, y, size):
    return 0 <= x < size and 0 <= y < size

def explode(grid, i, j, size):
    explosion_size = grid[i][j]
    explode_set = set()
    explode_set.add((i, j))
    if explosion_size > 1:
        for k in range(1, explosion_size):
            for direction in range(4):
                ni = i + k * dx[direction]
                nj = j + k * dy[direction]
                if in_range(ni, nj, size):
                    explode_set.add((ni, nj))
    for (x, y) in explode_set:
        grid[x][y] = 0
    return grid

def apply_gravity(grid, size):
    for col in range(size):
        new_col = []
        for row in range(size-1, -1, -1):
            if grid[row][col] != 0:
                new_col.append(grid[row][col])
        for row in range(size-1, -1, -1):
            if new_col:
                grid[row][col] = new_col.pop(0)
            else:
                grid[row][col] = 0
    return grid

def calculate(grid, size):
    count = 0
    for u in range(size):
        for y in range(size):
            for direction in range(4):
                ni = u + dx[direction]
                nj = y + dy[direction]
                if in_range(ni, nj, size):
                    if grid[u][y] == grid[ni][nj]:
                        count += 1
    return count // 2  # 각 쌍을 두 번 세므로 반으로 나눔

def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    num_list = []
    
    for i in range(n):
        for j in range(n):
            grid_copy = copy.deepcopy(grid)
            exploded_grid = explode(grid_copy, i, j, n)
            gravitied_grid = apply_gravity(exploded_grid, n)
            num_pairs = calculate(gravitied_grid, n)
            num_list.append(num_pairs)
    
    print(max(num_list))

if __name__ == "__main__":
    main()