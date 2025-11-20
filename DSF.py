# N-Queens Problem using Backtracking

N = 8  # Size of chessboard (8x8)

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

# Check if a queen can be placed safely
def is_safe(board, row, col):
    # Check column
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Solve recursively using backtracking
def solve_n_queens(board, col):
    if col >= N:
        print("One possible solution:\n")
        print_solution(board)
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_n_queens(board, col + 1):
                return True
            board[i][col] = 0  # Backtrack
    return False

# Driver Code
board = [[0 for _ in range(N)] for _ in range(N)]
print("\n--- Solving the 8-Queens Problem using Backtracking ---\n")

if not solve_n_queens(board, 0):
    print("No solution exists.")
else:
    print("✅ 8 Queens placed successfully!")
