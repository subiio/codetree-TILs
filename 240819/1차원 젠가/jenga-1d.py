n = int(input())
grid = []
for _ in range(n):
    grid.append(int(input()))


s1,e1 = map(int,input().split())
s2,e2 = map(int,input().split())
list_h = []
list_h.append([s1,e1])
list_h.append([s2,e2])
def make_grid(grid,s,e):
    temp = []
    for i in range(0,s-1):
        temp.append(grid[i])
    for j in range(e,len(grid)):
        temp.append(grid[j])
    
    return temp
for i in range(len(list_h)):
    grid = make_grid(grid,list_h[i][0],list_h[i][1])

print(len(grid))
for k in range(len(grid)):
    print(grid[k])