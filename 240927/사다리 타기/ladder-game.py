import copy
n,m = map(int,input().split())

ladder_list = []

init_number_list = []
for i in range(1,n+1):
    init_number_list.append(i)

for _ in range(m):
    ladder_list.append(list(map(int,input().split())))

def ladder_tagi(number_list,ladder):
    number_list2 = copy.deepcopy(number_list)
    ladder = sorted(ladder,key = lambda x: x[1])
    for i in range(len(ladder)):
        first_ind = ladder[i][0] -1
        second_ind = ladder[i][0]
        tmp = number_list2[second_ind]
        number_list2[second_ind] = number_list2[first_ind]
        number_list2[first_ind] = tmp
    return number_list2

min_len = 1000000000000000000000000
laddergrid = []
def backtracking(cur_num,end_grid,init_grid): 
    global min_len, ladder_list, laddergrid

    if  ladder_tagi(copy.deepcopy(init_number_list), init_grid)== end_grid:
        min_len = min(min_len, len(init_grid))
        return
    

    for i in range(cur_num, m):
        init_grid.append(ladder_list[i])
        backtracking(cur_num+1, end_grid, init_grid)
        init_grid.pop()
        
        

    


end_grid = ladder_tagi(init_number_list, ladder_list)
backtracking(0, end_grid,[])

print(min_len)