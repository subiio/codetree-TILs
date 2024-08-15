N,M,Q = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

wind_list = []
for _ in range(Q):
    wind_list.append(list(map(int,input().split())))

#### first 

def rotation(grid,r1,c1,r2,c2):
    ## r1 , r1 + 1 , r2
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    temp = []
    for j in range(c1, c2 + 1):
        temp.append(grid[r1][j])
    for i in range(r1+1, r2+1):
        temp.append(grid[i][c2])
    for k in range(c2-1, c1 , -1):
        temp.append(grid[r2][k])
    for l in range(r2, r1, -1):
        temp.append(grid[l][c1])
    length = 0
    # print("length of temp: ", temp)
    for r in range(c1+1, c2+1):
        # print("r: ", r-(c1+1))
        length = r-(c1+1)
  
        grid[r1][r] = temp[length]
    for n in range(r1+1, r2+1):
        # print("n: ", n) 
        # print("n: ", r2-(r1+1) + 1)
        length += 1
        # print("length2: ", length)
        grid[n][c2] = temp[length]
    
    for t in range(c2-1,c1, -1):
        # print("t: ", t)
        
        length += 1
        # print("length 22:", length)
        grid[r2][t] = temp[length]

    for q in range(r2, r1-1, -1):
        # print("q: ", q)
     
        length += 1

        grid[q][c1] = temp[length]
    
    return grid

def find_adj(grid,r,c,N,M):
    adj = []
    if 0 <= r <= N-1 and 0<= c-1 <= M-1:
        adj.append([r,c-1])
    if 0 <= r+1 <= N-1 and 0 <= c <= M-1:
        adj.append([r+1,c])
    if 0 <= r <= N-1 and 0 <= c+1 <= M-1:
        adj.append([r, c+1])
    if 0 <= r-1 <= N-1 and 0 <= c <= M-1:
        adj.append([r-1, c])
    return adj


for i in range(len(wind_list)):
    grid = rotation(grid,wind_list[i][0],wind_list[i][1],wind_list[i][2],wind_list[i][3])
    r1 = wind_list[i][0] -1
    c1 = wind_list[i][1] - 1
    r2 = wind_list[i][2] - 1
    c2 = wind_list[i][3] - 1
    grid_list = []

    for j in range(r1,r2+1):
        for k in range(c1,c2+1):
            list_adj = find_adj(grid,j,k,N,M)
            sum_1 = grid[j][k]
            for l in list_adj:
                sum_1 += grid[l[0]][l[1]]
            grid_list.append(((sum_1)//(len(list_adj)+1)))
                
    # for j in range(c1, c2 + 1):
    #     list_adj = find_adj(grid,r1,j,N,M)
    #     # print("list_adj: ",list_adj)
    #     sum_1 = grid[r1][j]
    #     for k in list_adj:
    #         sum_1 += grid[k[0]][k[1]]
    #     grid_list.append(((sum_1)//(len(list_adj)+1)))

    # for b in range(r1+1, r2+1):
    #     list_adj = find_adj(grid,b,c2,N,M)
    #     sum_2 = grid[b][c2]
    #     for k in list_adj:
    #         sum_2 += grid[k[0]][k[1]]
    #     grid_list.append(((sum_2)//(len(list_adj)+1)))
    # for k in range(c2-1, c1 , -1):
    #     list_adj = find_adj(grid,r2,k,N,M)
    #     sum_3 = grid[r2][k]
    #     for p in list_adj:
    #         sum_3 += grid[p[0]][p[1]]
    #     grid_list.append(((sum_3)//(len(list_adj)+1)))
    # for l in range(r2, r1, -1):
    #     list_adj = find_adj(grid,l,c1,N,M)
    #     sum_4 = grid[l][c1]
    #     for k in list_adj:
    #         sum_4 += grid[k[0]][k[1]]
    #     grid_list.append(((sum_4)//(len(list_adj)+1)))
    # length = 0
    # for r in range(c1, c2+1):
    #     # print("r: ", r-(c1+1))
    #     length = r-(c1+1)+1
    #     # print("grid_pixel: ", r1,r)
    #     # print("length: ", length)
    #     grid[r1][r] = grid_list[length]
    # for n in range(r1+1, r2+1):
    #     # print("n: ", n) 
    #     # print("n: ", r2-(r1+1) + 1)
    #     length += 1
    #     # print("length2: ", length)
    #     # print("grid_pixel: ", n,c2)
    #     # print("length: ", length)
    #     grid[n][c2] = grid_list[length]
    
    # for t in range(c2-1,c1, -1):
    #     # print("t: ", t)
        
    #     length += 1
    #     # print("length 22:", length)
    #     # print("grid_pixel: ",r2, t)
    #     # print("length: ", length)
    #     grid[r2][t] = grid_list[length]

    # for q in range(r2, r1, -1):

    #     # print("q: ", q)
     
    #     length += 1
    #     # print("grid_pixel: ",q,c1)
    #     # print("length: ", length)
    #     grid[q][c1] = grid_list[length]
    length = 0
    for x in range(r1,r2+1):
        for y in range(c1,c2+1):
            grid[x][y] = grid_list[length]
            length += 1
            
    
    



for i in range(N):
    for j in range(M):
        print(grid[i][j],end = " ")
    print()