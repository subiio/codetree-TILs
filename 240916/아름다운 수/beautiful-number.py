n = int(input())

answer = []

count = 0
def solution(curr_num):
    global count
    if curr_num == n:
        count += 1
    elif curr_num > n:
        pass
    else:
        for i in range(1,5):
            if i == 1:
                answer.append(i)
                solution(curr_num + 1)
                answer.pop()
            elif i == 2:
                answer.append(i)
                answer.append(i)
                solution(curr_num + 2)
                answer.pop()
            elif i == 3:
                answer.append(i)
                answer.append(i)
                answer.append(i) 
                solution(curr_num + 3)
                answer.pop()
            elif i == 4:
                answer.append(i)
                answer.append(i)
                answer.append(i)
                answer.append(i)
                solution(curr_num + 4)
                answer.pop()
solution(0)
print(count)