from collections import deque

class WaterJugsBFS:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.steps = []

    def bfs(self):
        queue = deque([(0, 0)])  # Start with both jugs empty
        visited = set()

        while queue:
            jug1, jug2 = queue.popleft()
            self.steps.append((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                return (jug1, jug2)

            # Fill jug1
            if (self.jug1_capacity, jug2) not in visited:
                queue.append((self.jug1_capacity, jug2))
                visited.add((self.jug1_capacity, jug2))

            # Fill jug2
            if (jug1, self.jug2_capacity) not in visited:
                queue.append((jug1, self.jug2_capacity))
                visited.add((jug1, self.jug2_capacity))

            # Empty jug1
            if (0, jug2) not in visited:
                queue.append((0, jug2))
                visited.add((0, jug2))

            # Empty jug2
            if (jug1, 0) not in visited:
                queue.append((jug1, 0))
                visited.add((jug1, 0))

            # Pour jug1 to jug2
            pour_amount = min(jug1, self.jug2_capacity - jug2)
            if (jug1 - pour_amount, jug2 + pour_amount) not in visited:
                queue.append((jug1 - pour_amount, jug2 + pour_amount))
                visited.add((jug1 - pour_amount, jug2 + pour_amount))

            # Pour jug2 to jug1
            pour_amount = min(jug2, self.jug1_capacity - jug1)
            if (jug1 + pour_amount, jug2 - pour_amount) not in visited:
                queue.append((jug1 + pour_amount, jug2 - pour_amount))
                visited.add((jug1 + pour_amount, jug2 - pour_amount))

        return None, None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jugs_bfs = WaterJugsBFS(jug1_capacity, jug2_capacity, target)
solution = water_jugs_bfs.bfs()

# Display steps
print("BFS Steps:")
for i, (jug1, jug2) in enumerate(water_jugs_bfs.steps):
    print(f"Step {i + 1}: Jug1={jug1}, Jug2={jug2}")

# Display solution
if solution:
    print("\nBFS Solution:")
    print(f"Target amount of water {target} reached!")
else:
    print("\nBFS Solution:")
    print("Target amount of water cannot be reached.")
