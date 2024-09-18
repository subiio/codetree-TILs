N = int(input())
stu_list = []
for _ in range(N):
    stu_list.append(list(map(int,input().split())))

# N = 4
# stu_list = [[1,5],[1,7],[3,6],[1,10]]


sorted_list = []

while N != len(sorted_list):
    min_ind = 0
    for i in range(len(stu_list)):
        if stu_list[i][0] < stu_list[min_ind][0]:
            min_ind = i
        elif stu_list[i][0] == stu_list[min_ind][0]:
            if stu_list[i][1] > stu_list[min_ind][1]:
                min_ind = i
            else:
                pass
        else:
            pass
    sorted_list.append(stu_list[min_ind])
    stu_list.pop(min_ind)

for i in range(1,len(sorted_list)+1):
    ind = i -1
    print(sorted_list[ind][0],sorted_list[ind][1], i)