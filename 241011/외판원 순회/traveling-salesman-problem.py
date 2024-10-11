n = int(input())
grid= []
for _ in range(n):
    grid.append(list(map(int,input().split())))

visited = [False for _ in range(n+1)]

answer= [1]

min_cost = 1000000
def backtracking(curr_num):
    global min_cost
    if curr_num == n-1:
        sum_number = 0
       
        for k in range(0,n):
            if k == n-1:
                sum_number += grid[answer[k]-1][0]
            else:
                # print(answer)
                sum_number += grid[answer[k]-1][answer[k+1]-1]
        min_cost = min(sum_number, min_cost)

        return

    for i in range(2,n+1):
        if visited[i] == True:
            continue
        
        visited[i] = True
        answer.append(i)
        backtracking(curr_num+1)
        answer.pop()
        visited[i] = False


backtracking(0)
        
print(min_cost)