import sys

def dijkstra(graph,source):
    n=len(graph)
    dist = [sys.maxsize]*n
    visited = [False]*n

    dist[source]=0

    for _ in range(n):
        min_dist = sys.maxsize
        u=-1
        for i in range(n):
            if not visited[i] and dist[i]<min_dist:
                min_dist = dist[i]
                u=i

        visited[u]=True

        for v in range(n):
            if graph[u][v]>0 and not visited[v]:
                if dist[v]>dist[u] + graph[u][v]:
                    dist[v]=dist[u]+graph[u][v]

    print("Vertex\tDistance from Source") 
    for i in range(n):
            print(i,"\t",dist[i]) 

graph = [
    [0, 10, 0, 5, 0],
    [10, 0, 1, 2, 0],
    [0, 1, 0, 9, 4],
    [5, 2, 9, 0, 2],
    [0, 0, 4, 2, 0]
]

dijkstra(graph, 0)
          