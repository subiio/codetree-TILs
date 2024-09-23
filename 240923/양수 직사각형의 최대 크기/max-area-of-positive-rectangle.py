n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

# n,m = 4,5
# grid = [[6,-2,4,-3,1],[3,6,7,-4,1],[6,1,8,15,-5],[3,-5,1,16,3]]

# 1 부분집합을 다 구한다.

def generate_all_rectangles(grid,n,m):
    rectangles = []

    for start_row in range(n):
        for end_row in range(start_row, n):
            for start_col in range(m):
                for end_col in range(start_col, m):
                    subgrid =[]
                    ifelse = 1
                    for r in range(start_row, end_row +1):
                        row = grid[r][start_col:end_col + 1]
                        subgrid.append(row)

                        if any(element <= 0 for element in row):
                            ifelse = False
                            break
                    
                    if ifelse:
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