n, m = map(int,input().split())
suyeol = []
for _ in range(n):
    suyeol.append(list(map(int,input().split())))


def count_numbers(a):
    list = []
    for i in range(1,101):
        list.append(a.count(i))
    list2 = []
    for j in range(len(list)):
        if list[j] >= m:
            list2.append(j+1)
    count1 = 0
    for k in list2:
        for l in a:
            if l != k:
                count1 = 0
            else:
                count1 += 1
                if count1 >= m:
                    return True


    return False

for i in range(n):
    list = []
    for j in range(n):
        list.append(suyeol[j][i])

        if j == n-1:
            suyeol.append(list)

count = 0
for i in suyeol:
    hi = count_numbers(i)
    if hi == True:
        count += 1
if len(suyeol) == 1:
    print(2)
else:
    print(count)



# #######
# [0][0],[1][0],[2][0]
# [0][1],[1][1],[2][1]
# [0][2],
# #######