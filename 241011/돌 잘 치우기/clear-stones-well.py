from collections import deque
import copy


n,k,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))
start_point = []
for _ in range(k):
    start_point.append(list(map(int,input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

q = deque()

def in_range(x,y):
    return (0<= x < n) and (0 <= y < n)



def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == True or grid[x][y] == 1:
        return False
    return True

def push(x,y):
    visited[x][y] = True
    q.append((x,y))


def bfs():

    dxs, dys = [1,0,-1,0],[0,1,0,-1]

    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y)

def find_ind(grid):
    result = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                result.append([i,j])
    return result

def find_sublist(list,idx,current,result):
    if idx == m:
        result.append(current[:])

    
    for i in range(idx, len(list)):
        current.append(list[i])
        find_sublist(list,idx+1,current,result)
        current.pop()
    
    

    

list_list = find_ind(grid)

result = []
sublist = find_sublist(list_list,0,[],result)



max_number = 0
for j in result:
    count = 0
    pyeong_list = copy.deepcopy(grid)
    visited = [[False for _ in range(n)] for _ in range(n)]
    for k in range(len(j)):
        ind_x, ind_y = j[k][0], j[k][1]
        pyeong_list[ind_x][ind_y] = 0
    for i in start_point:
        x,y = i[0], i[1]
        push(x,y)
        bfs()

    for t in range(n):
        for r in range(n):
            if visited[t][r] == True:
                count += 1
    max_number = max(max_number,count)

print(max_number)