n,m = map(int,input().split())
# n,m = 2,1
# n,m = 1,1
num_list= list(map(int,input().split()))
# num_list = [0]
# num_list = [1,2]
def xor(num1,num2):
    cnt = 1
    sum_number = 0
    num_list_1 = []
    num_list_2 = []
    while not (num1== 0 and num2== 0):
        num_list_1.append(num1 % 2)
        num_list_2.append(num2 % 2)
        num1 = num1//2 
        num2 = num2 // 2
    for i in range(len(num_list_1)):
        if num_list_1[i] == num_list_2[i]:
            sum_number += 0
        else:
            sum_number += 2**i
        
    return sum_number

max_num = 0
num_list2 = []
def backtracking(curnum,idx):
    global max_num
    if curnum == m:
        # print(num_list2)
        if m == 1:
            temp = num_list2[0]
        elif m == 2:
            temp = xor(num_list2[0],num_list2[1])
        else:
            first_num = num_list2[0]
            second_num = num_list2[1]
            temp = xor(first_num,second_num)
            for j in range(3,m):
                temp = xor(temp,num_list2[j])
        max_num = max(temp,max_num)
        return
        
    
    for i in range(idx,n):
        num_list2.append(num_list[i])
        backtracking(curnum + 1, i+1)
        num_list2.pop()    

backtracking(0,0) 
print(max_num)