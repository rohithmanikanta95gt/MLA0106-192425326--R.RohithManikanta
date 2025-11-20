# Water Jug Problem - AI State Space Search

from collections import deque

def water_jug_problem(capacity_x, capacity_y, target):
    visited = set()                 # Track visited states
    queue = deque([(0, 0)])         # Start with empty jugs
    path = []                       # To record sequence of steps

    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path.append((x, y))

        # Goal check
        if x == target or y == target:
            print("\nPath to reach the goal:")
            for state in path:
                print(state)
            print(f"\n✅ Goal reached! ({x}, {y})")
            return

        # Possible moves
        moves = [
            (capacity_x, y),           # Fill 4-gallon jug
            (x, capacity_y),           # Fill 3-gallon jug
            (0, y),                    # Empty 4-gallon jug
            (x, 0),                    # Empty 3-gallon jug
            (x - min(x, capacity_y - y), y + min(x, capacity_y - y)),  # Pour X → Y
            (x + min(y, capacity_x - x), y - min(y, capacity_x - x))   # Pour Y → X
        ]

        for move in moves:
            if move not in visited:
                queue.append(move)

# Run for 4-gallon and 3-gallon jugs
print("\n--- Solving the Water Jug Problem ---\n")
water_jug_problem(4, 3, 2)
