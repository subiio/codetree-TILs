n = int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))


def find_index(n,grid):
    key = [[-1, 1],[-1, -1],[1,-1],[1, 1]]
    index_list = []
    for i in range(n):
        for j in range(n):
            first = [i+key[0][0], j+key[0][1]]
            second = [first[0]+key[1][0], first[1] + key[1][1]]
            third = [second[0]+key[2][0], second[1] + key[2][1]]
            forth = [third[0] + key[3][0], third[1] + key[3][1]]
            if (0 <= first[0] <= n and 0<= first[1] <= n) and (0 <= second[0] <= n and 0<= second[1] <= n) and (0 <= third[0] <= n and 0<= third[1] <= n) and (0 <= forth[0] <= n and 0<= forth[1] <= n):
                index_list.append([i,j])
    return index_list
    

def find_max(center, grid):
    key = [[-1, 1],[-1, -1], [1, -1], [1, 1]]
    tmp = center
    indexing = [tmp]
     
    for i in range(len(key)):
        flag = True
        while 0 <= tmp[0] + key[i][0] < n and 0 <= tmp[1] + key[i][1] < n and flag == True :
            if i <= 2 and 0 <= tmp[0] + key[i][0] + key[i+1][0] < n and 0 <= tmp[1] + key[i][1] + key[i+1][1] < n :
                tmp = [tmp[0] + key[i][0], tmp[1] + key[i][1]]
                indexing.append(tmp)
            elif  i ==3 and not(tmp[0] ==  center[0] and tmp[1] == center[1]) :
                
                tmp = [tmp[0] + key[i][0], tmp[1] + key[i][1]]
                indexing.append(tmp)
                
            else:
                flag= False
    max_number = 0
    for j in indexing:
        
        max_number += grid[j[0]][j[1]]
    return max_number - grid[center[0]][center[1]]

indexing_list = find_index(n,grid)
maxi = 0
tmpi = 0
for i in indexing_list:
    tmpi = find_max(i, grid)
    maxi = max(maxi, tmpi)

print(maxi)