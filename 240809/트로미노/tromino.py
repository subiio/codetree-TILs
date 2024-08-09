n,m = map(int,input().split())

grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))



# key1 [[i, j],[i, j+1], [i+1, j]]
# key2 [[i, j], [i+1, j], [i+1, j+1]]
# key3 [[i+1,j], [i+1,j+1], [i, j+1]]
# key4 [[i, j], [i, j+1], [i+1, j+1]]
# key5 [[i,j], [i, j+1], [i, j+2]]
# key6 [[i, j], [i+1, j], [i+2, j]]
key = [ [[0, 0],[0, 1], [1, 0]],
    [[0, 0], [1, 0], [1, 1]],
    [[1,0], [1,1], [0, 1]],
    [[0, 0], [0, 1], [1, 1]],
    [[0,0], [0, 1], [0, 2]],
    [[0,0], [1, 0], [2, 0]]
]


def find_max(key,grid):
    # example of key : [[0,0], [0,1], [1,0]]
    n = len(grid[0])
    m = len(grid)
    first = key[0]
    second = key[1]
    third = key[2]
    maximum = 0
    tmp = 0
    for i in range(n):
        for j in range(m):
            if ((i+first[0]) < m and (j+first[1]) < n) and ((i+second[0]) < m and (j+second[1] < n) and ((i+third[0])< m and (j+third[1]) < n)):
                tmp = (grid[i+first[0]][j+first[1]] + grid[i+second[0]][j+second[1]] + grid[i+third[0]][j+third[1]])
            maximum = max(maximum, tmp)
    return maximum

maximum_list = []
for k in range(len(key)):
    maximum_list.append(find_max(key[k], grid))

print(max(maximum_list))