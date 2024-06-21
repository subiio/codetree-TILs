from collections import deque

N,K = map(int,input().split())
dq = deque()

for i in range(N):
    dq.append(i+1)


while len(dq) != 0:
    for _ in range(K-1):
        dq.append(dq[0])
        dq.popleft()
    print(dq[0], end = ' ')
    dq.popleft()