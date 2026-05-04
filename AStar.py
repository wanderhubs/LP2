import heapq

def heuristic(a, b):
    # Manhattan Distance = row difference + column difference
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    # open_list stores nodes as (f_value, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # came_from stores previous node to create final path
    came_from = {}

    # g_score stores cost from start to each node
    g_score = {start: 0}

    while open_list:
        # Pick node with smallest f value
        current_f, current = heapq.heappop(open_list)

        # If goal is reached, create final path
        if current == goal:
            path = []

            # Go backward from goal to start
            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            # Reverse path to get start to goal
            path.reverse()
            return path

        # Current position
        x, y = current

        # Possible movements: up, down, left, right
        neighbors = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]

        # Check all neighbours
        for neighbor in neighbors:
            nx, ny = neighbor

            # Skip if outside grid
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                continue

            # Skip if obstacle
            if grid[nx][ny] == 1:
                continue

            # Moving one step costs 1
            new_g_score = g_score[current] + 1

            # If neighbour is new or we found shorter path
            if neighbor not in g_score or new_g_score < g_score[neighbor]:
                g_score[neighbor] = new_g_score

                # f = g + h
                f_score = new_g_score + heuristic(neighbor, goal)

                # Add neighbour to open list
                heapq.heappush(open_list, (f_score, neighbor))

                # Remember path
                came_from[neighbor] = current

    # If path not found
    return None


# Small example grid
# 0 = free path
# 1 = obstacle

grid = [
    [0, 0, 0],
    [1, 0, 1],
    [0, 0, 0]
]

start = (0, 0)
goal = (2, 2)

path = astar(grid, start, goal)

print("Shortest Path:")
print(path)