class NQueensDFS:
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

    def dfs(self, board, row):
        if row == self.N:  # If all queens are placed, add solution
            return [board[:]]

        solutions = []
        for col in range(self.N):
            if self.is_safe(board, row, col):
                board.append(col)  # Add valid column to the board
                solutions.extend(self.dfs(board, row + 1))
                board.pop()  # Backtrack

        return solutions

    def find_solutions(self):
        return self.dfs([], 0)

# Example usage:
n = 8  # Size of the chessboard
n_queens_dfs = NQueensDFS(n)

# Solve using DFS
dfs_solutions = n_queens_dfs.find_solutions()
print("DFS Solutions:")
for solution in dfs_solutions:
    print(solution)
