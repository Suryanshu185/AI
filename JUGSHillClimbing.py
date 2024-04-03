class WaterJugsHillClimbing:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.steps = []

    def heuristic(self, state):
        # Use the sum of differences between current and target water levels as the heuristic
        jug1_diff = abs(self.target - state[0])
        jug2_diff = abs(self.target - state[1])
        return jug1_diff + jug2_diff

    def get_neighbors(self, state):
        neighbors = []
        jug1, jug2 = state

        # Fill jug1
        if jug1 < self.jug1_capacity:
            neighbors.append((self.jug1_capacity, jug2))

        # Fill jug2
        if jug2 < self.jug2_capacity:
            neighbors.append((jug1, self.jug2_capacity))

        # Empty jug1
        if jug1 > 0:
            neighbors.append((0, jug2))

        # Empty jug2
        if jug2 > 0:
            neighbors.append((jug1, 0))

        # Pour jug1 to jug2
        if jug1 > 0 and jug2 < self.jug2_capacity:
            amount_to_pour = min(jug1, self.jug2_capacity - jug2)
            neighbors.append((jug1 - amount_to_pour, jug2 + amount_to_pour))

        # Pour jug2 to jug1
        if jug2 > 0 and jug1 < self.jug1_capacity:
            amount_to_pour = min(jug2, self.jug1_capacity - jug1)
            neighbors.append((jug1 + amount_to_pour, jug2 - amount_to_pour))

        return neighbors

    def hill_climbing(self, start_state):
        current_state = start_state
        current_heuristic = self.heuristic(start_state)
        self.steps.append(start_state)

        while True:
            neighbors = self.get_neighbors(current_state)
            best_neighbor = None
            best_neighbor_heuristic = float('-inf')

            for neighbor in neighbors:
                neighbor_heuristic = self.heuristic(neighbor)
                if neighbor_heuristic > best_neighbor_heuristic:
                    best_neighbor = neighbor
                    best_neighbor_heuristic = neighbor_heuristic

            if best_neighbor_heuristic <= current_heuristic:
                # Local maximum reached
                break

            current_state = best_neighbor
            current_heuristic = best_neighbor_heuristic
            self.steps.append(current_state)

        return current_state

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2
start_state = (0, 0)

water_jugs_hill_climbing = WaterJugsHillClimbing(jug1_capacity, jug2_capacity, target)
solution = water_jugs_hill_climbing.hill_climbing(start_state)

# Display steps
print("Hill Climbing Steps:")
for i, (jug1, jug2) in enumerate(water_jugs_hill_climbing.steps):
    print(f"Step {i + 1}: Jug1={jug1}, Jug2={jug2}")

# Display solution
print("\nHill Climbing Solution:")
if solution == (0, 0):
    print("Target amount of water cannot be reached.")
else:
    print(f"Target amount of water {target} reached!")
