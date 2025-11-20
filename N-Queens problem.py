# N-Queens using Hill Climbing (Pure Python)

# Count number of attacking pairs
def heuristic(state):
    h = 0
    n = len(state)

    for i in range(n):
        for j in range(i+1, n):
            # Same row
            if state[i] == state[j]:
                h += 1
            # Same diagonal
            if abs(state[i] - state[j]) == abs(i - j):
                h += 1

    return h


# Generate best possible neighbor
def best_neighbor(state):
    n = len(state)
    best_state = list(state)
    best_h = heuristic(state)

    for col in range(n):
        original_row = state[col]

        for row in range(n):
            if row != original_row:
                new_state = list(state)
                new_state[col] = row
                h = heuristic(new_state)

                if h < best_h:
                    best_h = h
                    best_state = new_state

    return best_state, best_h


# Print chessboard
def print_board(state):
    n = len(state)
    for r in range(n):
        row = ""
        for c in range(n):
            if state[c] == r:
                row += "Q "
            else:
                row += ". "
        print(row)
    print()


# Hill Climbing algorithm (with random restart)
def hill_climbing(n):
    # Random initial placement (one queen per column)
    state = [0] * n
    for i in range(n):
        state[i] = i % n  # Simple deterministic placement

    print("\n--- N-Queens using Hill Climbing ---\n")
    print("Initial State Heuristic:", heuristic(state))

    while True:
        current_h = heuristic(state)
        neighbor, neighbor_h = best_neighbor(state)

        if neighbor_h >= current_h:
            # Reached local optimum or solution
            print("\nFinal State (Heuristic =", current_h, "):\n")
            print_board(state)
            if current_h == 0:
                print("✔ Solution Found!")
            else:
                print("⚠ Stuck in Local Minimum!")
            return

        state = neighbor


# Run for N = 8 (change N for larger boards)
hill_climbing(8)
