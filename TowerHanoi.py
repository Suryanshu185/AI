from queue import Queue, LifoQueue, PriorityQueue
import heapq

class State:
    def __init__(self, disks, source, target, auxiliary, steps=0, parent=None):
        self.disks = disks
        self.source = source
        self.target = target
        self.auxiliary = auxiliary
        self.steps = steps
        self.parent = parent

def is_valid_move(state, source, target):
    if not source or (target and target[-1] < source[-1]):
        return False
    return True

def move_disk(source, target):
    disk = source.pop()
    target.append(disk)

def tower_of_hanoi_bfs(num_disks, source, target, auxiliary):
    initial_state = State(list(range(num_disks, 0, -1)), source, target, auxiliary)
    visited = set()
    queue = Queue()
    queue.put(initial_state)

    while not queue.empty():
        current_state = queue.get()
        visited.add(tuple(current_state.disks))

        if current_state.target == list(range(num_disks, 0, -1)):
            return current_state.steps

        for source, target in [(current_state.source, current_state.auxiliary),
                               (current_state.source, current_state.target),
                               (current_state.auxiliary, current_state.source),
                               (current_state.auxiliary, current_state.target),
                               (current_state.target, current_state.source),
                               (current_state.target, current_state.auxiliary)]:
            if is_valid_move(current_state.disks, source, target):
                new_disks = current_state.disks[:]
                move_disk(source, target)
                new_state = State(new_disks, current_state.source, current_state.target, current_state.auxiliary,
                                  current_state.steps + 1, current_state)
                if tuple(new_disks) not in visited:
                    queue.put(new_state)

    return -1

def tower_of_hanoi_dfs(num_disks, source, target, auxiliary):
    initial_state = State(list(range(num_disks, 0, -1)), source, target, auxiliary)
    visited = set()
    stack = [initial_state]

    while stack:
        current_state = stack.pop()
        visited.add(tuple(current_state.disks))

        if current_state.target == list(range(num_disks, 0, -1)):
            return current_state.steps

        for source, target in [(current_state.source, current_state.auxiliary),
                               (current_state.source, current_state.target),
                               (current_state.auxiliary, current_state.source),
                               (current_state.auxiliary, current_state.target),
                               (current_state.target, current_state.source),
                               (current_state.target, current_state.auxiliary)]:
            if is_valid_move(current_state.disks, source, target):
                new_disks = current_state.disks[:]
                move_disk(source, target)
                new_state = State(new_disks, current_state.source, current_state.target, current_state.auxiliary,
                                  current_state.steps + 1, current_state)
                if tuple(new_disks) not in visited:
                    stack.append(new_state)

    return -1

def tower_of_hanoi_best_first(num_disks, source, target, auxiliary):
    initial_state = State(list(range(num_disks, 0, -1)), source, target, auxiliary)
    visited = set()
    queue = PriorityQueue()
    queue.put((0, initial_state))

    while not queue.empty():
        _, current_state = queue.get()
        visited.add(tuple(current_state.disks))

        if current_state.target == list(range(num_disks, 0, -1)):
            return current_state.steps

        for source, target in [(current_state.source, current_state.auxiliary),
                               (current_state.source, current_state.target),
                               (current_state.auxiliary, current_state.source),
                               (current_state.auxiliary, current_state.target),
                               (current_state.target, current_state.source),
                               (current_state.target, current_state.auxiliary)]:
            if is_valid_move(current_state.disks, source, target):
                new_disks = current_state.disks[:]
                move_disk(source, target)
                new_state = State(new_disks, current_state.source, current_state.target, current_state.auxiliary,
                                  current_state.steps + 1, current_state)
                if tuple(new_disks) not in visited:
                    queue.put((current_state.steps + 1, new_state))

    return -1

def tower_of_hanoi_astar(num_disks, source, target, auxiliary):
    initial_state = State(list(range(num_disks, 0, -1)), source, target, auxiliary)
    visited = set()
    open_list = []
    heapq.heappush(open_list, (0, initial_state))

    while open_list:
        _, current_state = heapq.heappop(open_list)
        visited.add(tuple(current_state.disks))

        if current_state.target == list(range(num_disks, 0, -1)):
            return current_state.steps

        for source, target in [(current_state.source, current_state.auxiliary),
                               (current_state.source, current_state.target),
                               (current_state.auxiliary, current_state.source),
                               (current_state.auxiliary, current_state.target),
                               (current_state.target, current_state.source),
                               (current_state.target, current_state.auxiliary)]:
            if is_valid_move(current_state.disks, source, target):
                new_disks = current_state.disks[:]
                move_disk(source, target)
                new_state = State(new_disks, current_state.source, current_state.target, current_state.auxiliary,
                                  current_state.steps + 1, current_state)
                if tuple(new_disks) not in visited:
                    heapq.heappush(open_list, (current_state.steps + 1 + heuristic(new_state), new_state))

    return -1

def tower_of_hanoi_hill_climbing(num_disks, source, target, auxiliary):
    pass  # Hill climbing algorithm implementation not provided in this example

# Example usage:
num_disks = 3
source_peg = []
target_peg = []
auxiliary_peg = []
minimum_moves_bfs = tower_of_hanoi_bfs(num_disks, source_peg, target_peg, auxiliary_peg)
minimum_moves_dfs = tower_of_hanoi_dfs(num_disks, source_peg, target_peg, auxiliary_peg)
minimum_moves_best_first = tower_of_hanoi_best_first(num_disks, source_peg, target_peg, auxiliary_peg)
minimum_moves_astar = tower_of_hanoi_astar(num_disks, source_peg, target_peg, auxiliary_peg)
minimum_moves_hill_climbing = tower_of_hanoi_hill_climbing(num_disks, source_peg, target_peg, auxiliary_peg)

print(f"Minimum moves using BFS: {minimum_moves_bfs}")
print(f"Minimum moves using DFS: {minimum_moves_dfs}")
print(f"Minimum moves using Best First Search: {minimum_moves_best_first}")
print(f"Minimum moves using A*: {minimum_moves_astar}")
print(f"Minimum moves using Hill Climbing:
