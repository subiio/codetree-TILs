from collections import deque

dq = deque()

N = int(input())
for i in range(N):
    command = input()
    try:
        comm,key = command.split()
    except:
        comm = command

    if comm == "push":
        dq.append(key)
    elif comm == "front":
        print(dq[0])
    elif comm == "size":
        print(len(dq))
    elif comm == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    else:
        print(dq.popleft())