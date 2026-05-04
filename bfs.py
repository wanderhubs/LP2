from collections import deque

def bfs(start, adj, V):
    visited = [False] * V
    queue = deque()

    visited[start] = True
    queue.append(start)

    print("BFS Traversal:")

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)


V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

adj = [[] for _ in range(V)]

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)   

start = int(input("Enter starting node: "))

bfs(start, adj, V)

