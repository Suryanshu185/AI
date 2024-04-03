# Answer 2: Best First Search
from collections import deque
import queue

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def calculate_heuristic(self):
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row, col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - row) + abs(j - col)
        return total_distance

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic


class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state

    def generate_next_states(self, state):
        i, j = self.find_empty(state)
        next_states = []
        if i > 0:
            next_state = [row[:] for row in state]
            next_state[i][j], next_state[i - 1][j] = next_state[i - 1][j], next_state[i][j]
            next_states.append(('UP', next_state))
        if i < 2:
            next_state = [row[:] for row in state]
            next_state[i][j], next_state[i + 1][j] = next_state[i + 1][j], next_state[i][j]
            next_states.append(('DOWN', next_state))
        if j > 0:
            next_state = [row[:] for row in state]
            next_state[i][j], next_state[i][j - 1] = next_state[i][j - 1], next_state[i][j]
            next_states.append(('LEFT', next_state))
        if j < 2:
            next_state = [row[:] for row in state]
            next_state[i][j], next_state[i][j + 1] = next_state[i][j + 1], next_state[i][j]
            next_states.append(('RIGHT', next_state))
        return next_states

    def find_empty(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def is_goal_state(self, state):
        return state == self.goal_state


class Search:

    def best_first_search(initial_state, goal_state):
        puzzle = Puzzle(initial_state, goal_state)
        visited = set()
        priority_queue = queue.PriorityQueue()
        priority_queue.put(PuzzleNode(initial_state))

        while not priority_queue.empty():
            node = priority_queue.get()
            state = node.state

            if puzzle.is_goal_state(state):
                return Search.get_path(node)

            visited.add(tuple(map(tuple, state)))

            for action, next_state in puzzle.generate_next_states(state):
                if tuple(map(tuple, next_state)) not in visited:
                    child_node = PuzzleNode(next_state, node, action, node.cost + 1)
                    priority_queue.put(child_node)
                    visited.add(tuple(map(tuple, next_state)))

        return None

    def get_path(node):
        path = []
        while node:
            path.append((node.action, node.state))
            node = node.parent
        return path[::-1]


initial_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solution_path = Search.best_first_search(initial_state, goal_state)
if solution_path:
    print("Solution Path:")
    for step in solution_path:
        print(step)
else:
    print("Best-First Search failed to find a solution.")
