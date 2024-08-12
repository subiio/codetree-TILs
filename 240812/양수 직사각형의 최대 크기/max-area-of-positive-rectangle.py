n,m = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

def find_max(center,grid,n,m):
    searchable_list = []
    for i in range(n):
        for j in range(m):
            tmp = []
            if i >= 1 and j >=1:
                for k in range(i+1):
                    for l in range(j+1):
                        if 0 <= (center[0] + k) < n and 0<= (center[1] + l) < n:
                            if grid[center[0] + k][center[1] + l] > 0:
                                tmp.append([center[0] + k,center[1] + l])
                            else:
                                tmp.append(-1)
                        else:
                            tmp.append(-1)
                if -1 in tmp:
                    tmp = [-1]        
            searchable_list.append(tmp)
    # print("searchable_list:", searchable_list)
    return searchable_list
center = []
for i in range(n):
    for j in range(m):
        center.append([i,j])


max_length = 0
for i in center:
    searchable_list = find_max(i,grid,n,m)
    # print(searchable_list)
    for j in searchable_list:
        # print(len(j))
        tmp = len(j)
        max_length = max(max_length,tmp)

print(max_length)