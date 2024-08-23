n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int,input().split())))

r,c = map(int,input().split())

# n = grid[r-1][c-1]

def range_check(grid,r,c):
    right,left,low,high = 0,0,0,0
    
    for i in range(1,n):
        # print("i: ", i)
        if 0 <= r-1 < n and 0 <= c-1+i  < n:
            right += 1
        else:
            break
    for j in range(1, n):
        # print("j: ", j)
        if 0 <= r-1 < n and 0 <= c-1-i  < n:
            left += 1
        else:
            break
    for k in range(1, n):
        # print("k: ", k)
        if 0 <= r-1+i < n and 0 <= c-1  < n:
            low += 1
        else:
            break
    for l in range(1,n):
        if 0 <= r-1-l < n and 0 <= c-1  < n:
            high += 1
        else:
            break
    return right,left,low,high


a = grid[r-1][c-1]

right,left,low,high = range_check(grid,r,c)

grid_list = []

grid_list.append([r-1,c-1])
right_final,left_final,low_final,high_final = 0,0,0,0
if right >= a-1:
    right_final = a-1
else:
    right_final = right
for i in range(1,right_final+1):
    grid_list.append([r-1,c-1+i])
if left >= a-1:
    left_final = a-1
else:
    left_final = left
for j in range(1,left_final+1):
    grid_list.append([r-1, c-1-j])

if low >= a-1:
    low_final = a-1
else:
    low_final = right
for k in range(1,low_final+1):
    grid_list.append([r-1+k, c-1])
if high >= a-1:
    high_final = a-1
else:
    high_final = high
for l in range(1,high_final+1):
    grid_list.append([r-1-l, c-1])
# print(grid_list)
for p in grid_list:
    a = p[0]
    b = p[1]
    grid[a][b] = 0

for y in grid_list:
    d = y[0]
    b = y[1]
    aing_list1 = []
    aing_list2 = []
    if b < c-1 or b > c-1:
    
        # print("d: ", b)
        for i in range(d,0,-1):
            grid[i][b] = grid[i-1][b]
        grid[0][b] = 0
    else:
        aing_list1.append(d)
        aing_list2.append(b)

# print(grid)
min_range = min(aing_list1)
max_range = max(aing_list2)

range_list = []
for t in range(0,(min_range)):
    range_list.append(grid[t][c-1])

for u in range(max_range+1,n):
    range_list.append(grid[u][c-1])


for q in range(n-1, n-len(range_list)-1, -1):
    # print("q: ", q)
    # print(q-n+len(range_list)-1)
    grid[q][c-1] = range_list[q-n+len(range_list)-1]

# print(grid)

for w in range(n):
    for e in range(n):
        print(grid[w][e], end= " ")
    print()