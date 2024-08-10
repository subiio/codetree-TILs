n,m = map(int,input().split())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))


#######################
#        [1, 1]
# [2, 0] [2, 1] [2, 2]
#        [3, 1] 
#######################
# 0 <= K <= 19
#
# i = 0 , 
#
#
#
#######################


def find_key(K,center):
    key_list = [center]
    key = [[0,1],[0,-1],[1,0],[-1,0]] 
    if K == 0:
        return key_list
    for i in range(1, K+1):
        for j in range(len(key_list)):
            number1 = [key_list[j][0] + key[0][0], key_list[j][1] + key[0][1]]
            number2 = [key_list[j][0] + key[1][0], key_list[j][1] + key[1][1]]
            number3 = [key_list[j][0] + key[2][0], key_list[j][1] + key[2][1]]
            number4 = [key_list[j][0] + key[3][0], key_list[j][1] + key[3][1]]
            if not (number1 in key_list):
                key_list.append(number1)
            if not (number2 in key_list):
                key_list.append(number2)
            if not (number3 in key_list):
                key_list.append(number3)
            if not (number4 in key_list):
                key_list.append(number4)

    return key_list

K = len(grid)
max_gold = 0
for i in range(K):
    cost = i*i + (i+1)*(i+1)
    for j in range(n):
        for k in range(n):
            tmp = 0
            key_list = find_key(i, [j,k])
            for l in key_list:
                if (0 <= l[0] < n) and (0 <= l[1] < n) :
                    if grid[l[0]][l[1]] == 1:
                        tmp += 1
            if tmp*m >=  cost and tmp > max_gold:
                max_gold = tmp

print(max_gold)




        
    


# def find_max()