n = int(input())
num_list = list(map(int,input().split()))
# n = 9
# num_list = [1,5,2,9,7,4,6,10,11]
new_list = []

for i in range(1, len(num_list)+1):
    ind = i-1
    new_list.append(num_list[ind])
    if i % 2 == 1:
        length = len(new_list)
        new_ind = length//2
        new_list = sorted(new_list)
        print(new_list[new_ind], end = " ")