vertices = int(input())
edges_count = int(input())

edges = []
for _ in range(edges_count):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

parent = [i for i in range(vertices)]

def find(v):# use to avoid cycles and keep track of group
    while parent[v] != v:
        v = parent[v]
    return v

mst_cost = 0

for w, u, v in edges:
    if find(u) != find(v):
        print(u, "-", v, ":", w)
        mst_cost += w
        parent[find(v)] = find(u)#union

print("Total cost:", mst_cost)