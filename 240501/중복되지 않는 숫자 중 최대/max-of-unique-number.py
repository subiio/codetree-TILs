N = input()
N = int(N)
list1 = list(map(int,input().split()))
list2 = []
for i in list1:
    count = 0
    for j in list1:
        if i == j :
            count += 1
    if count == 1:
        list2.append(i)
if len(list2) == 0:
    print(-1)
else:
    print(max(list2))



# max_list = max(list1)

# count = 0
# for i in list1:
#     if i == max_list: