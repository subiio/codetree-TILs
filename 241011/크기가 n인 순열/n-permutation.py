n = int(input())

answer = []

visited = [False for _ in range(n+1)]

def print_answer():
    for i in answer:
        print(i,end= " ")
    print()
def backtracking(curr_num):
    if curr_num == n+1:
        print_answer()
        return 


    for i in range(1, n+1):
        if visited[i] == True:
            continue

        visited[i] = True
        answer.append(i)
        backtracking(curr_num+1)

        answer.pop()

        visited[i] = False

backtracking(1)