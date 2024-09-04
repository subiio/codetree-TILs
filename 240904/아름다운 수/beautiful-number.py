n = int(input())
answer = []


count = 0
def print_answer():
    global count
    count += 1
    # for i in answer:
    #     print(i, end = "")
    # print()

def choose(curr_num):
    if curr_num == n+1:
        print_answer()
        return
    
    for j in range(1,n+1):
        # print("j: ", j)
        if j == 1:
            if (n-len(answer)) >= 1:

                answer.append(j)
                choose(curr_num + 1)

                answer.pop()
            else:
                pass
        elif j == 2:
            if (n-len(answer)) >=2:
                answer.append(j)
                answer.append(j)
                choose(curr_num+ 2)
                answer.pop()
                answer.pop()
            else:
                pass

        elif j == 3:
            if (n-len(answer)) >= 3:
                answer.append(j)
                answer.append(j)
                answer.append(j)
                choose(curr_num + 3)
                answer.pop()
                answer.pop()
                answer.pop()
            else:
                pass
        elif j == 4:
            if (n-len(answer)) >= 4:
                answer.append(j)
                answer.append(j)
                answer.append(j)
                answer.append(j)
                choose(curr_num + 4)
                answer.pop()
                answer.pop()
                answer.pop()
                answer.pop()
            else:
                pass
        
    return 

choose(1)
print(count)