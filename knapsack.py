from queue import PriorityQueue
from collections import deque

class KnapsackProblem:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity

    def bfs(self):
        queue = deque([(0, 0, [])])  # (total_value, total_weight, chosen_items)

        best_value = 0
        best_solution = []

        while queue:
            total_value, total_weight, chosen_items = queue.popleft()

            if total_value > best_value:
                best_value = total_value
                best_solution = chosen_items

            for item in self.items:
                if item not in chosen_items and total_weight + item[1] <= self.capacity:
                    new_chosen_items = chosen_items + [item]
                    new_total_value = sum(item[0] for item in new_chosen_items)
                    new_total_weight = sum(item[1] for item in new_chosen_items)

                    queue.append((new_total_value, new_total_weight, new_chosen_items))

        return best_solution

    def dfs(self):
        stack = [(0, 0, [])]  # (total_value, total_weight, chosen_items)

        best_value = 0
        best_solution = []

        while stack:
            total_value, total_weight, chosen_items = stack.pop()

            if total_value > best_value:
                best_value = total_value
                best_solution = chosen_items

            for item in self.items[::-1]:
                if item not in chosen_items and total_weight + item[1] <= self.capacity:
                    new_chosen_items = chosen_items + [item]
                    new_total_value = sum(item[0] for item in new_chosen_items)
                    new_total_weight = sum(item[1] for item in new_chosen_items)

                    stack.append((new_total_value, new_total_weight, new_chosen_items))

        return best_solution

    def best_first(self):
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, []))  # (total_value, total_weight, chosen_items)

        best_value = 0
        best_solution = []

        while not priority_queue.empty():
            total_value, total_weight, chosen_items = priority_queue.get()

            if total_value > best_value:
                best_value = total_value
                best_solution = chosen_items

            for item in self.items:
                if item not in chosen_items and total_weight + item[1] <= self.capacity:
                    new_chosen_items = chosen_items + [item]
                    new_total_value = sum(item[0] for item in new_chosen_items)
                    new_total_weight = sum(item[1] for item in new_chosen_items)

                    priority_queue.put((-new_total_value, new_total_weight, new_chosen_items))

        return best_solution

    def a_star(self):
        priority_queue = PriorityQueue()
        priority_queue.put((0, 0, []))  # (total_value, total_weight, chosen_items)

        best_value = 0
        best_solution = []

        while not priority_queue.empty():
            total_value, total_weight, chosen_items = priority_queue.get()

            if total_value > best_value:
                best_value = total_value
                best_solution = chosen_items

            for item in self.items:
                if item not in chosen_items and total_weight + item[1] <= self.capacity:
                    new_chosen_items = chosen_items + [item]
                    new_total_value = sum(item[0] for item in new_chosen_items)
                    new_total_weight = sum(item[1] for item in new_chosen_items)

                    priority_queue.put((-new_total_value - (self.capacity - new_total_weight), new_total_weight, new_chosen_items))

        return best_solution

    def hill_climbing(self):
        current_value = 0
        current_weight = 0
        chosen_items = []

        for item in self.items:
            if current_weight + item[1] <= self.capacity:
                current_value += item[0]
                current_weight += item[1]
                chosen_items.append(item)

        return chosen_items

# Example usage:
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50

knapsack_problem = KnapsackProblem(items, capacity)

# Solve using BFS
bfs_solution = knapsack_problem.bfs()
print("BFS Solution:", bfs_solution)

# Solve using DFS
dfs_solution = knapsack_problem.dfs()
print("DFS Solution:", dfs_solution)

# Solve using Best First
best_first_solution = knapsack_problem.best_first()
print("Best First Solution:", best_first_solution)

# Solve using A*
a_star_solution = knapsack_problem.a_star()
print("A* Solution:", a_star_solution)

# Solve using Hill Climbing
hill_climbing_solution = knapsack_problem.hill_climbing()
print("Hill Climbing Solution:", hill_climbing_solution)
