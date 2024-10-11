n = int(input())

visited = [False for _ in range(n+1)]

answer= []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()

def backtracking(curr_num):
    if curr_num == n+1:
        print_answer()
        return 
    
    for i in range(n,0,-1):
        if visited[i]:
            continue
        
        visited[i] = True
        answer.append(i)
        backtracking(curr_num+1)
        answer.pop()
        visited[i] = False


backtracking(1)