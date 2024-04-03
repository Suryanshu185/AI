class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.g_score = 0
        self.h_score = self.calculate_heuristic()
        self.f_score = self.g_score + self.h_score

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def calculate_heuristic(self):
        # Manhattan Distance heuristic
        total_distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    row, col = divmod(self.state[i][j] - 1, 3)
                    total_distance += abs(i - row) + abs(j - col)
        return total_distance


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

    def a_star_search(self, initial_state, goal_state):
        puzzle = Puzzle(initial_state, goal_state)
        open_set = {PuzzleNode(initial_state)}
        closed_set = set()

        while open_set:
            current_node = min(open_set, key=lambda node: node.f_score)
            open_set.remove(current_node)
            closed_set.add(current_node)

            if puzzle.is_goal_state(current_node.state):
                return Search.get_path(current_node)

            for neighbor in puzzle.generate_next_states(current_node.state):
                neighbor_node = PuzzleNode(neighbor[1], current_node, neighbor[0])
                if neighbor_node in closed_set:
                    continue

                tentative_g_score = current_node.g_score + 1

                if neighbor_node not in open_set or tentative_g_score < neighbor_node.g_score:
                    neighbor_node.parent = current_node
                    neighbor_node.g_score = tentative_g_score
                    open_set.add(neighbor_node)

        return None

    def get_path(node):
        path = []
        while node:
            path.append((node.action, node.state))
            node = node.parent
        return path[::-1]


initial_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

solution_path = Search().a_star_search(initial_state, goal_state)
if solution_path is not None:
    print("Solution Path:")
    for step in solution_path:
        print(step)
else:
    print("A* Search failed to find a solution.")
