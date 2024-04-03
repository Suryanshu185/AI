from collections import deque

class NQueensBFS:
    def __init__(self, N):
        self.N = N

    def is_safe(self, board, row, col):
        # Check if there is a queen in the same column or diagonals
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def bfs(self):
        solutions = []
        queue = deque([([], 0)])  # Start with an empty board at row 0

        while queue:
            board, row = queue.popleft()
            if row == self.N:  # If all queens are placed, add solution
                solutions.append(board)
                continue

            for col in range(self.N):
                if self.is_safe(board, row, col):
                    queue.append((board + [col], row + 1))  # Add valid column to the board

        return solutions

# Example usage:
n = 8  # Size of the chessboard
n_queens_bfs = NQueensBFS(n)

# Solve using BFS
bfs_solutions = n_queens_bfs.bfs()
print("BFS Solutions:")
for solution in bfs_solutions:
    print(solution)
