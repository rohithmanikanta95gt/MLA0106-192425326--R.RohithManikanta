import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

# Helper function to convert state to tuple (for hashing)
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Find the blank (0) position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // 3
                target_y = (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

# Get all possible neighbor states
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in DIRECTIONS:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Pretty print puzzle
def print_state(state):
    for row in state:
        print(" ".join(str(x) if x != 0 else '_' for x in row))
    print()

# A* Search Algorithm (shows full path)
def a_star(start):
    start_tuple = to_tuple(start)
    goal_tuple = to_tuple(GOAL_STATE)
    pq = []
    heapq.heappush(pq, (manhattan_distance(start), 0, start, []))
    visited = set()

    while pq:
        est_total, cost, current, path = heapq.heappop(pq)
        current_tuple = to_tuple(current)

        if current_tuple in visited:
            continue
        visited.add(current_tuple)
        new_path = path + [current]

        # Goal check
        if current == GOAL_STATE:
            print("🎯 Goal reached in", cost, "moves!\n")
            print("🧩 Steps from start to goal:\n")
            for step, state in enumerate(new_path):
                print(f"Step {step}:")
                print_state(state)
            return

        # Explore neighbors
        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                total_cost = cost + 1
                est = total_cost + manhattan_distance(neighbor)
                heapq.heappush(pq, (est, total_cost, neighbor, new_path))

    print("No solution found.")

# Example usage
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

a_star(initial_state)
