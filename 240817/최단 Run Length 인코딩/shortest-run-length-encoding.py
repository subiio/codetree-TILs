A = input()
A = list(A)

# print(A)

def shift(A):
    temp = A[-1]
    for i in range(len(A)-1,0,-1):
        A[i] = A[i-1]
    A[0] = temp

    return A


def RunLengthEncoding(A):
    Run_list = []
    count = 1
    for j in range(len(A)):
        if j == 0 :
            Run_list.append(A[j])
        else:
            if A[j] == A[j-1] and not(j == len(A) -1):
                count += 1
            elif (A[j] == A[j-1]) and (j == len(A)-1):
                count += 1
                Run_list.append(count)

            elif A[j] != A[j-1] and not(j == len(A)-1):
                Run_list.append(count)
                Run_list.append(A[j])
                count = 1
            else:
                Run_list.append(count)
                Run_list.append(A[j])
                count = 1
                Run_list.append(count)

    return len(Run_list)

                 
Run_length_list = []
for i in range(len(A)):
    if i == 0:
        Run_length_list.append(RunLengthEncoding(A))
    else:
        A = shift(A)
        Run_length_list.append(RunLengthEncoding(A))

print(min(Run_length_list))