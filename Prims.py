INF = 999999

n = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")
graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

selected = [False] * n
selected[0] = True

edges = 0
total_cost = 0

print("Edges in Minimum Spanning Tree:")

while edges < n - 1:
    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", graph[x][y])
    total_cost += graph[x][y]
    selected[y] = True
    edges += 1

print("Total cost of MST:", total_cost)