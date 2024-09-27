n,m = map(int,input().split())

ladder_list = []

init_number_list = [1,2,3,4]

for _ in range(m):
    ladder_list.append(list(map(int,input().split())))

def ladder_tagi(init_number_list,ladder):
    sorted(ladder,key = lambda x: ladder[1])
    print(ladder)

ladder_tagi(init_number_list, ladder_list)