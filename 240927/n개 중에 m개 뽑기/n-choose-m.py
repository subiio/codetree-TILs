N,M = map(int,input().split())

num_list =[]

def print_answer():
    for elem in num_list:
        print(elem, end = " ")
    print()


def backtracking(curnum,idx):
    if curnum == M:
        print_answer()
        return
    
    for i in range(idx+1,N+1):
        num_list.append(i)
        backtracking(curnum + 1, i)
        num_list.pop()
        


backtracking(0, 0)