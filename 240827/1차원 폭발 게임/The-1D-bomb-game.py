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
            remove_index.append(grid[len(grid)-1])
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
            for j in range(0, remove_index[i]):
                grid_2.append(grid[j])
            
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
    if len(grid) == 0:
        print(0)
        break
    if count == 0:
        isStop = True
    else:
        isStop = False