n =  int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

def reached_destination(x,y):
    return (x < 0 or x >= n or y < 0 or y >= n)



dx = [1,-1,0,0]
dy = [0,0,1,-1]
start_point = []
for i in range(n):
    start_point.append([0,i,0]) # 3번째 인덱스는 초기 이동 방향

for i in range(n):
    start_point.append([n-1,i,1])

for i in range(n):
    start_point.append([i,0,2])

for i in range(n):
    start_point.append([i,n-1,3])
time_list = []
for i in start_point:
    start_ind_x = i[0]
    start_ind_y = i[1]
    start_ind_yaw = i[2]
    ind_x = start_ind_x
    ind_y = start_ind_y
    prev_ind_yaw = start_ind_yaw
    ind_yaw = start_ind_yaw
    time = 1
    while not reached_destination(ind_x,ind_y):
        if grid[ind_x][ind_y] == 0:
            dxs = dx[ind_yaw]
            dys = dy[ind_yaw]
            ind_x += dxs
            ind_y += dys
            prev_ind_yaw = ind_yaw
            ind_yaw = ind_yaw
            time += 1
        
        elif grid[ind_x][ind_y] == 1:
            # 북쪽에서 올 때
            if prev_ind_yaw == 0:
                ind_yaw = 3
            # 남쪽에서 올 때
            elif prev_ind_yaw == 1:
                ind_yaw = 2

            # 서쪽에서 올 때
            elif prev_ind_yaw == 2:
                ind_yaw = 1
            # 동쪽에서 올 때
            else:
                ind_yaw = 0
            dxs = dx[ind_yaw]
            dys = dy[ind_yaw]
            ind_x += dxs
            ind_y += dys
            prev_ind_yaw = ind_yaw
            ind_yaw = ind_yaw
            time += 1

        elif grid[ind_x][ind_y] == 2:
            # 북쪽에서 올 때
            if prev_ind_yaw == 0:
                ind_yaw = 2
            # 남쪽에서 올 때
            elif prev_ind_yaw == 1:
                ind_yaw = 3

            # 서쪽에서 올 때
            elif prev_ind_yaw == 2:
                ind_yaw = 0
            # 동쪽에서 올 때
            else:
                ind_yaw = 1

            dxs = dx[ind_yaw]
            dys = dy[ind_yaw]
            ind_x += dxs
            ind_y += dys
            prev_ind_yaw = ind_yaw
            ind_yaw = ind_yaw
            time += 1
    # print("time: ", time)
    time_list.append(time)

print(max(time_list))