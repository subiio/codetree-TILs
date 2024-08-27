N,M = map(int,input().split())

grid = []
for _ in range(N):
    grid.append(int(input()))



IsStop = False

while not IsStop:
    count = 0
    iter_count = 1
    remove_index = []
    for i in range(len(grid)-1):
        # print("i: ", i)
        # print("iter_count: ", iter_count)
        if grid[i] == grid[i+1]:
            iter_count += 1
            if iter_count == 2:
                remove_index.append(i)
            else:
                pass
        else:
            if iter_count >= M:
                remove_index.append(i)
                count += 1
            else:
                try:
                    remove_index.pop()
                except:
                    pass
                
        
            iter_count = 1
    if iter_count != 1:
        if iter_count >= M:
            remove_index.append(len(grid)-1)
            count += 1
        else:
            try:
                remove_index.pop()
            except:
                pass
    # print("count : ", count)
    # print("remove: ", remove_index)
    if len(remove_index) != 0:
        length_remove_index = len(remove_index)
        grid_2 = []
        for i in range(0,length_remove_index,2):
            # print("tlqkf: ", i)
            if i == 0:
                for j in range(0, remove_index[i]):
                    grid_2.append(grid[j])
            else:
                try:
                    for j in range(remove_index[i-1]+1,remove_index[i]):
                        grid_2.append(grid[j])
                except:
                    pass

            
            try:
                for k in range(remove_index[i+1]+1,remove_index[i+2]):
                    grid_2.append(grid[k])
            except:
                for k in range(remove_index[i+1]+1,len(grid)):
                    grid_2.append(grid[k])
        grid = grid_2
    
    else:
        grid = grid
    # print("grid: ", grid)

    if count == 0:
        IsStop = True
    else:
        IsStop = False

print(len(grid))

try:
    for i in range(len(grid)):
        print(grid[i])
except:
    pass