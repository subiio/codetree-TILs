N,M = map(int,input().split())
start_point = []
end_point = []

for _ in range(M):
    a,b = map(int,input().split())
    start_point.append(a)
    end_point.append(b)

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(vertex):
    count = 1
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

    return count



for start, end in zip(start_point, end_point):
    graph[start].append(end)
    graph[end].append(start)


root_vertex = 1

print(dfs(root_vertex))