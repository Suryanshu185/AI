import random

class NQueensHillClimbing:
    def __init__(self, N):
        self.N = N

    def initial_state(self):
        return tuple(random.randint(0, self.N - 1) for _ in range(self.N))

    def attacking_queens(self, state):
        attacks = 0
        for i in range(self.N):
            for j in range(i + 1, self.N):
                if state[i] == state[j] or abs(i - j) == abs(state[i] - state[j]):
                    attacks += 1
        return attacks

    def neighbors(self, state):
        neighbor_states = []
        for i in range(self.N):
            for j in range(self.N):
                if j != state[i]:
                    neighbor = list(state)
                    neighbor[i] = j
                    neighbor_states.append(tuple(neighbor))
        return neighbor_states

    def hill_climbing(self):
        current_state = self.initial_state()
        current_attacks = self.attacking_queens(current_state)

        while True:
            neighbor_states = self.neighbors(current_state)
            best_neighbor = current_state
            best_attacks = current_attacks

            for neighbor_state in neighbor_states:
                neighbor_attacks = self.attacking_queens(neighbor_state)
                if neighbor_attacks < best_attacks:
                    best_neighbor = neighbor_state
                    best_attacks = neighbor_attacks

            if best_attacks >= current_attacks:
                # Local optimum reached
                return current_state
            else:
                current_state = best_neighbor
                current_attacks = best_attacks

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
n_queens_hill_climbing = NQueensHillClimbing(n)

# Solve using Hill Climbing
solution = n_queens_hill_climbing.hill_climbing()
print("Hill Climbing Solution:")
n_queens_hill_climbing.print_board(solution)
