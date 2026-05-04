def dfs(node, visited, adj):
    visited[node] = True
    print(node, end=" ")
    
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, adj)


V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))

adj = [[] for _ in range(V)]

print("Enter edges (u v):")
for _ in range(E):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * V

start = int(input("Enter starting node: "))

print("DFS Traversal:")
dfs(start, visited, adj)