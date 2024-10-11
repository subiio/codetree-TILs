n = int(input())

grid = []

for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = [False for _ in range(n)]

answer = []
max_number =0
def backtracking(curr_num):
    global max_number
    if curr_num == n :
        max_number = max(sum(answer), max_number)
        return

    
    for j in range(n):
        if visited[j] == True:
            continue
            
        visited[j] = True
        answer.append(grid[curr_num][j])
        backtracking(curr_num + 1)
        answer.pop()
        visited[j] = False


backtracking(0)

print(max_number)