K,N = map(int,input().split())

answer = []

def print_answer():
    for elem in answer:
        print(elem, end = " ")
    print()


def solution(curr_num):
    if curr_num == N+1:
        print_answer()
        return

    else:
        for i in range(1,K+1):
            if (curr_num <= 2) or (answer[-1] != i and answer[-2] != i) or (answer[-1] != i):
                answer.append(i)
                solution(curr_num + 1)
                answer.pop()

solution(1)