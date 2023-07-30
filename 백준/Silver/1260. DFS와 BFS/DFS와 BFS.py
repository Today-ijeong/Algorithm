from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
for i in range(1, n + 1):
    graph[i].sort()
dfs_sol = 0
bfs_sol = 0
def dfs(start):
    stack = []
    visit = [0 for _ in range(n + 1)]
    stack.append(start)
    while len(stack) > 0:
        curr = stack[-1]
        if visit[curr] == 0:
            print(curr, end=' ')
            visit[curr] = 1
        flag = False
        for nxt in graph[curr]:
            if visit[nxt] == 0:
                stack.append(nxt)
                flag = True
                break
        if not flag:
            stack.pop()
def bfs(start):
    queue = deque()
    visited = [0 for _ in range(n + 1)]
    queue.append(start)
    visited[start] = 1
    while len(queue) > 0:
        curr = queue[0]
        print(curr, end=' ')
        for nxt in graph[curr]:
            if visited[nxt] == 0:
                visited[nxt] = 1
                queue.append(nxt)
        queue.popleft()
dfs(v)
print()
bfs(v)