n = int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))


visited = [[False for _ in range(n)] for _ in range(n)]



def in_range(x,y):
    return (0 <= x < n) and (0 <= y < n)

def can_go(i,j,prev_number):
    
    if not in_range(i,j):
        return False
    if visited[i][j] == True or grid[i][j] != prev_number :
        return False
    return True
def available(x,y):
    if not in_range:
        return False
    if visited[x][y] == True:
        return False
    return True
count = 0
def dfs(x,y):

    global count
    dxs, dys = [1,0,-1,0],[0,1,0,-1]

    for dx,dy in zip(dxs,dys):
        new_x , new_y = x +dx , y + dy

        if can_go(new_x,new_y,grid[x][y]):
            visited[new_x][new_y] = True
            count += 1
            dfs(new_x,new_y)
result = []
for i in range(n):
    for j in range(n):
        if available(i,j):
            visited[i][j] = True
            count = 1
            dfs(i,j)
            result.append(count)

# print(result)

count2 = 0

for i in result:
    if i >= 4:
        count2 += 1

print(count2, end = " ")
print(max(result))