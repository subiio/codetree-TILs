n = int(input())

grid = []

def print_answer():
    print(len(grid))
answer = []
def backtracking(curr_num):
    if curr_num == n:
        answer.append(grid)
        return 
    for i in range(1, 5):
        if i == 1:
            if curr_num <= n -1:
                grid.append(i)
                backtracking(curr_num + 1)
                grid.pop()
            else:
                pass
        elif i == 2:
            if curr_num <= n -2:
                grid.append(i)
                grid.append(i)
                backtracking(curr_num + 2)
                grid.pop()
                grid.pop()
            else:
                pass
        elif i == 3:
            if curr_num <= n -3:
                grid.append(i)
                grid.append(i)
                grid.append(i)
                backtracking(curr_num + 3)
                grid.pop()
                grid.pop()
                grid.pop()
            else:
                pass
        elif i == 4:
            if curr_num <= n -4:
                grid.append(i)
                grid.append(i)
                grid.append(i)
                grid.append(i)
                backtracking(curr_num + 4)
                grid.pop()
                grid.pop()
                grid.pop()
                grid.pop()
            else:
                pass

backtracking(0)
print(len(answer))