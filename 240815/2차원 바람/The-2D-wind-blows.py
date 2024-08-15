N,M,Q = map(int,input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int,input().split())))

r1,c1,r2,c2 = map(int,input().split())

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
    print("length of temp: ", temp)
    for r in range(c1+1, c2+1):
        print("r: ", r)
        length = c2-(c1+1)+1
        for m in range(length):
            print("temp_ind1: ", m)
            grid[r1][r] = temp[m]
    length += c2-(c1+1)+1
    for n in range(r1+1, r2+1):
        print("n: ", n) 
        print("n: ", r2-(r1+1) + 1)
        for b in range(r2-(r1+1) + 1):
            print("temp_ind2: ", m)
            grid[n][c2] = temp[length+b]
    length += r2-(r1+1)+1
    print("length2: ", length)
    for t in range(c2-1,c1, -1):
        print("t: ", t)
        for e in range((c2-1)-c1):
            print("temp_ind3: ", length +e)
            grid[r2][t] = temp[length+e]
    length += ((c2-1)-c1)
    print("length3: ", length)
    for q in range(r2, r1-1, -1):
        print("q: ", q)
        for w in range(r2 - (r1-1)):
            print("temp_ind4: ", length + w)
            grid[q][c1] = temp[length + w]
    
    return grid

print(rotation(grid,r1,c1,r2,c2))