n,m,k = map(int,input().split())

moving = list(map(int,input().split()))

answer = []
count = 0
k_list = []
for l in range(k):
    k_list.append(1)

max_number = 0
def solution(curr_mov):
    global count, k_list, max_number
    if curr_mov == n:
        
        for elem in k_list:
            if elem >= m:
                count += 1
        if max_number < count:
            max_number = count
        count = 0
        return 

    else:
        
        for i in range(len(k_list)):
            prev_pos = k_list[i]
            k_list[i] += moving[curr_mov]
            solution(curr_mov + 1)
            k_list[i] = prev_pos
        
        
solution(0)
print(max_number)