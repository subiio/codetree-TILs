n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

   
# 1 부분집합을 다 구한다.

def generate_all_rectangles(grid,n,m):
    rectangles = []

    for start_row in range(n):
        for end_row in range(start_row, n):
            for start_col in range(m):
                for end_col in range(start_col, m):
                    subgrid =[]
                    for r in range(start_row, end_row +1):
                        row = grid[r][start_col:end_col + 1]
                        subgrid.append(row)
                    ifelse = 1
                    for k in subgrid:
                        for l in k:
                            if l <= 0:
                                ifelse = 0
                            else:
                                ifelse = 1
                    if ifelse == 1:
                        rectangles.append(subgrid)
                                

    return rectangles

all_rectangles = generate_all_rectangles(grid,n,m)

max_num = -1
for i in range(len(all_rectangles)):
    grid_length = 0
    # print("all_rectangles: ", all_rectangles[i])
    for j in all_rectangles[i]:
        grid_length += len(j)
    max_num = max(max_num, grid_length)
    # print("grid_length: ",grid_length)

print(max_num)