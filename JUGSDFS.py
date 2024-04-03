class WaterJugsDFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.steps = []

    def dfs(self):
        stack = [(0, 0)]  # Start with both jugs empty
        visited = set()

        while stack:
            jug1, jug2 = stack.pop()
            self.steps.append((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                return (jug1, jug2)

            visited.add((jug1, jug2))

            # Generate next possible states
            next_states = [
                (self.jug1_capacity, jug2),  # Fill jug1
                (jug1, self.jug2_capacity),  # Fill jug2
                (0, jug2),                    # Empty jug1
                (jug1, 0),                    # Empty jug2
                (max(0, jug1 - (self.jug2_capacity - jug2)), min(jug1 + jug2, self.jug2_capacity)),  # Pour jug1 to jug2
                (min(jug1 + jug2, self.jug1_capacity), max(0, jug2 - (self.jug1_capacity - jug1)))   # Pour jug2 to jug1
            ]

            # Add next states to stack if not visited
            for state in next_states:
                if state not in visited:
                    stack.append(state)
                    visited.add(state)

        return None, None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jugs_dfs = WaterJugsDFS(jug1_capacity, jug2_capacity, target)
solution = water_jugs_dfs.dfs()

# Display steps
print("DFS Steps:")
for i, (jug1, jug2) in enumerate(water_jugs_dfs.steps):
    print(f"Step {i + 1}: Jug1={jug1}, Jug2={jug2}")

# Display solution
if solution:
    print("\nDFS Solution:")
    print(f"Target amount of water {target} reached!")
else:
    print("\nDFS Solution:")
    print("Target amount of water cannot be reached.")
