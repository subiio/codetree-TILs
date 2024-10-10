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

    elif pyeongga_list[x][y] == 1 or visited[x][y] == True:
        return False
    return True

def push(x,y):
    visited[x][y] = True
    q.append((x,y))

def bfs():
    global count
    dxs, dys = [1,0,-1,0], [0,1,0,-1]

    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x,new_y):
                push(new_x,new_y)
                count += 1
def find_ind_1(grid):
    ind_list = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                ind_list.append([i,j])
    return ind_list

index_list = find_ind_1(grid)


# def find_list(ind_list,m):
#     start_ind = 0
#     list_holy = []
#     while start_ind != (len(ind_list) - m + 1):
#         start_ind += 1
def backtracking(ind_list,idx,current,result):

    result.append(current[:])

    for i in range(idx, len(ind_list)):
        current.append(ind_list[i])

        backtracking(ind_list, i + 1, current, result)

        current.pop()

def get_all_sublists(ind_list):
    result = []
    backtracking(ind_list,0, [], result)
    return result
        

sublist = get_all_sublists(index_list)
gwansim_list = []
for i in sublist:
    if len(i) == m:
        gwansim_list.append(i)
# print(gwansim_list)

max_number = 0
for j in gwansim_list:
    count = 1
    pyeongga_list = copy.deepcopy(grid)
    for k in range(len(j)):
        ind_x, ind_y  = j[k][0], j[k][1]
        pyeongga_list[ind_x][ind_y] = 0
        # count = 0
        for i in start_point:
            x,y = i[0]-1, i[1]-1 
            push(x,y)
            bfs()
    max_number = max(max_number,count)
            

print(max_number)