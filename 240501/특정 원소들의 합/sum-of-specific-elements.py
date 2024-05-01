list1 = []
for _ in range(4):
    a= list(map(int,input().split()))
    list1.append(a)


# list1[0][0] + ...
# list1[1][0] + list[1][1]
# list1[2][0] + list[2][1] + list[2][2]
sum1 = 0

for i in range(4):
    for j in range(0,i+1):
        sum1 += list1[i][j]

print(sum1)