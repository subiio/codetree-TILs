n, m = map(int,input().split())
suyeol = []
for _ in range(n):
    suyeol.append(list(map(int,input().split())))


def count_numbers(a):
    list2 = []
    for i in range(1,101):
        list2.append(a.count(i))
    list3 = []
    for j in range(len(list2)):
        if list2[j] >= m:
            list3.append(j+1)
    for k in list3:
        count1 = 0
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