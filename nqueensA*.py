import heapq

class NQueensAStar:
    def __init__(self, N):
        self.N = N

    def is_safe(self, board, row, col):
        # Check if there is a queen in the same column or diagonals
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == row - i:
                return False
        return True

    def heuristic(self, board, row):
        # Heuristic function: number of conflicts (attacking queens) in the current row
        conflicts = 0
        for i in range(row):
            if board[i] == board[row] or \
               abs(board[i] - board[row]) == row - i:
                conflicts += 1
        return conflicts

    def a_star_search(self):
        solutions = []
        heap = [(0, (), 0)]  # Priority queue: (heuristic value, board, row)

        while heap:
            _, board, row = heapq.heappop(heap)
            if row == self.N:  # If all queens are placed, add solution
                solutions.append(board)
                continue

            for col in range(self.N):
                if self.is_safe(board, row, col):
                    new_board = board + (col,)
                    heapq.heappush(heap, (row + 1 + self.heuristic(new_board, row), new_board, row + 1))

        return solutions

    def print_board(self, state):
        for row in range(self.N):
            queen_col = state[row]
            for col in range(self.N):
                if col == queen_col:
                    print("Q ", end="")
                else:
                    print(". ", end="")
            print()
        print()

# Example usage:
n = 8  # Size of the chessboard
n_queens_a_star = NQueensAStar(n)

# Solve using A* search
solutions = n_queens_a_star.a_star_search()
print("A* Search Solutions:")
for solution in solutions:
    n_queens_a_star.print_board(solution)
