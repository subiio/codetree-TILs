N,M = map(int,input().split())

visited = [False for _ in range(N+1)]

adj_list = [[False for _ in range(N+1)] for _ in range(N+1)]


for _ in range(M):
    a,b = map(int,input().split())
    adj_list[a][b] = 1
    adj_list[b][a] = 1

#  0 0 0 0 0 0 
#  0 0 1 1 0 0
#  0 1 0 1 0 0
#  0 1 1 0 0 0
#  0 0 0 0 0 1
#  0 0 0 0 1 0

VERTICES_NUM = N 


count = 0
def dfs(vertex):
    global count
    for curr_v in range(1, VERTICES_NUM + 1):
        if adj_list[vertex][curr_v] and not visited[curr_v]:
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

dfs(1)
if N == 1 or M == 0:
    print(0)
else:    
    print(count - 1)
print()
# def dfs(vertex):
#     for curr_v in graph[vertex]:
#         if not visited[curr_v]:
#             print(curr_v)
#             visited[curr_v] = True
#             dfs(curr_v)