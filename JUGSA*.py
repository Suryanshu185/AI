import heapq

class WaterJugsAStar:
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

    def total_cost(self, state, current_cost):
        return current_cost + self.heuristic(state)

    def a_star(self):
        priority_queue = [(self.total_cost((0, 0), 0), (0, 0, 0))]  # Start with both jugs empty and cost 0
        visited = set()

        while priority_queue:
            _, (jug1, jug2, cost) = heapq.heappop(priority_queue)
            self.steps.append((jug1, jug2))

            if jug1 == self.target or jug2 == self.target:
                return (jug1, jug2)

            visited.add((jug1, jug2))

            # Generate next possible states
            next_states = [
                (self.jug1_capacity, jug2, cost + 1),  # Fill jug1
                (jug1, self.jug2_capacity, cost + 1),  # Fill jug2
                (0, jug2, cost + 1),                    # Empty jug1
                (jug1, 0, cost + 1),                    # Empty jug2
                (max(0, jug1 - (self.jug2_capacity - jug2)), min(jug1 + jug2, self.jug2_capacity), cost + 1),  # Pour jug1 to jug2
                (min(jug1 + jug2, self.jug1_capacity), max(0, jug2 - (self.jug1_capacity - jug1)), cost + 1)   # Pour jug2 to jug1
            ]

            # Add next states to priority queue if not visited
            for state in next_states:
                if state[:2] not in visited:
                    heapq.heappush(priority_queue, (self.total_cost(state[:2], state[2]), state))
                    visited.add(state[:2])

        return None, None

# Example usage:
jug1_capacity = 4
jug2_capacity = 3
target = 2

water_jugs_a_star = WaterJugsAStar(jug1_capacity, jug2_capacity, target)
solution = water_jugs_a_star.a_star()

# Display steps
print("A* Steps:")
for i, (jug1, jug2) in enumerate(water_jugs_a_star.steps):
    print(f"Step {i + 1}: Jug1={jug1}, Jug2={jug2}")

# Display solution
if solution:
    print("\nA* Solution:")
    print(f"Target amount of water {target} reached!")
else:
    print("\nA* Solution:")
    print("Target amount of water cannot be reached.")
