N, S = map(int,input().split())
N_list = list(map(int,input().split()))

num_list = []


N_list_copy = N_list.copy()
N_list_copy_2 = N_list.copy()
min_number = 10000000
for i in range(len(N_list)):
    for j in range(i+1,len(N_list)):
        N_list_copy = N_list.copy()
        N_list_copy_2 = N_list.copy()
        a = N_list_copy.pop(i)
        b = N_list_copy_2.pop(j)
       
        sum_number = 0
        for k in N_list:
            if (k == a or k == b):
                pass
            else:
                sum_number += k
        if abs(sum_number - S) < min_number:
            min_number = abs(sum_number - S)

print(min_number)