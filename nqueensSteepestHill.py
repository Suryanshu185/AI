import random

class NQueensSteepestAscent:
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
        min_attacks = self.attacking_queens(state)

        for i in range(self.N):
            for j in range(self.N):
                if j != state[i]:
                    neighbor = list(state)
                    neighbor[i] = j
                    attacks = self.attacking_queens(tuple(neighbor))
                    if attacks < min_attacks:
                        neighbor_states = [tuple(neighbor)]
                        min_attacks = attacks
                    elif attacks == min_attacks:
                        neighbor_states.append(tuple(neighbor))

        return neighbor_states

    def steepest_ascent(self):
        current_state = self.initial_state()
        current_attacks = self.attacking_queens(current_state)

        while True:
            neighbor_states = self.neighbors(current_state)
            if not neighbor_states:
                return current_state

            best_neighbor = random.choice(neighbor_states)
            best_attacks = self.attacking_queens(best_neighbor)

            if best_attacks >= current_attacks:
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
n_queens_steepest_ascent = NQueensSteepestAscent(n)

# Solve using Steepest Ascent Hill Climbing
solution = n_queens_steepest_ascent.steepest_ascent()
print("Steepest Ascent Hill Climbing Solution:")
n_queens_steepest_ascent.print_board(solution)
