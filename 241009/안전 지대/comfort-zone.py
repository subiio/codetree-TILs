N,M = map(int,input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))


max_k = 0
for i in grid:
    max_k = max(max(i),max_k)

pyeongga_grid = [[0 for _ in range(M)] for _ in range(N)] 

visited = [[False for _ in range(M)] for _ in range(N)]


# print(pyeongga_grid)

def in_range(i,j):
    return (0 <= i < N) and (0 <= j < M)

def can_go(i,j):
    if not in_range(i,j):
        return False
    if visited[i][j] == True or pyeongga_grid[i][j] == 0:
        return False
    return True

count = 0
def dfs(x,y):
    global count
    dxs,dys = [1,0,-1,0],[0,1,0,-1]

    for dx, dy in zip(dxs,dys):
        new_x, new_y = x + dx , y + dy
        if can_go(new_x,new_y):
            count += 1
            # print("new_x: , new_y: ",new_x,new_y)
            visited[new_x][new_y] = True

            dfs(new_x,new_y)
        



answer = []

max_index = 1
max_number = 0
for i in range(1,max_k + 1):
    result = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for k in range(M):
            if grid[j][k] > i:
                pyeongga_grid[j][k] = 1
            else:
                pyeongga_grid[j][k] = 0
    
    for l in range(N):
        for e in range(M):
            if can_go(l,e) == 1:
                visited[l][e] = True
                count = 1
                dfs(l,e)
                # print("count: ", count)
                result.append(count)
    if len(result) > max_number:
        max_index = i
        max_number = len(result)
    elif len(result ) == max_number:
        pass

print(max_index, end =" ")
print(max_number)









# for i in range(n):
#     for j in range(n):
#         if available(i,j):

#             visited[i][j] = True
#             count = 1

#             dfs(i,j)

#             result.append(count)