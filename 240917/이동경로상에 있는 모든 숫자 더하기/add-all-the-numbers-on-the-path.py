N,T = map(int,input().split())

moving = input()
moving = list(moving)
grid = []
for i in range(N):
    grid.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [-1,0,1,0]

def in_range(x,y):
    return (0 <= x <= N-1) and (0 <= y <= N-1)


cur_ind = 0
dxs = dx[cur_ind]
dys = dy[cur_ind]
x = N//2
y = N//2
sum_number = grid[x][y]
for j in (moving):
    # print("x,y: ", x,y)
    if j == "R":
        try:
            
            # print("cur_ind: ", cur_ind)
            cur_ind += 1
            # if in_range(x+dx[cur_ind], y+dy[cur_ind]):
            #     dxs = dx[cur_ind]
            #     dys = dy[cur_ind]
            #     x += dxs
            #     y += dys
            #     sum_number += grid[y][x]

        except:
            pass

    elif j == "F":
        try:
            # print("cur_ind: ", cur_ind)
            if in_range(x+dx[cur_ind], y+dy[cur_ind]):
                dxs = dx[cur_ind]
                dys = dy[cur_ind]
                x += dxs
                y += dys
                sum_number += grid[y][x]
            else:
                pass
        except:
            pass

    elif j == "L":
        try:
            # print("cur_ind: ", cur_ind)
            cur_ind -= 1
            # if in_range(x+dx[cur_ind], y+dy[cur_ind]):
            #     dxs = dx[cur_ind]
            #     dys = dy[cur_ind]
            #     x += dxs
            #     y += dys
        except:
            pass
    else:
        pass

print(sum_number)