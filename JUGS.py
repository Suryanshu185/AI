class Jug:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_volume = 0

    def fill(self):
        self.current_volume = self.capacity

    def empty(self):
        self.current_volume = 0

    def transfer(self, other_jug):
        if self.current_volume <= other_jug.capacity - other_jug.current_volume:
            transferred_volume = self.current_volume
        else:
            transferred_volume = other_jug.capacity - other_jug.current_volume

        self.current_volume -= transferred_volume
        other_jug.current_volume += transferred_volume


def simulate_water_transfer():
    jug_4 = Jug(4)
    jug_3 = Jug(3)
    steps = []

    # Fill jug_4
    jug_4.fill()
    steps.append(f"Step 1: Fill jug(4)={jug_4.current_volume}, Fill jug(3)={jug_3.current_volume}")

    # Transfer water from jug_4 to jug_3
    jug_4.transfer(jug_3)
    steps.append(f"Step 2: Transfer from jug(4) to jug(3). Jug(4)={jug_4.current_volume}, Jug(3)={jug_3.current_volume}")

    # Empty jug_3
    jug_3.empty()
    steps.append(f"Step 3: Empty jug(3). Jug(4)={jug_4.current_volume}, Jug(3)={jug_3.current_volume}")

    # Transfer water from jug_4 to jug_3
    jug_4.transfer(jug_3)
    steps.append(f"Step 4: Transfer from jug(4) to jug(3). Jug(4)={jug_4.current_volume}, Jug(3)={jug_3.current_volume}")

    # Fill jug_4
    jug_4.fill()
    steps.append(f"Step 5: Fill jug(4)={jug_4.current_volume}, Fill jug(3)={jug_3.current_volume}")

    # Transfer water from jug_4 to jug_3
    jug_4.transfer(jug_3)
    steps.append(f"Step 6: Transfer from jug(4) to jug(3). Jug(4)={jug_4.current_volume}, Jug(3)={jug_3.current_volume}")

    # The final state of jug_4 will have exactly 2 liters of water
    return jug_4.current_volume, steps


# Run the simulation
result, steps = simulate_water_transfer()

# Print each step
for step in steps:
    print(step)

print(f"Final volume in jug_4: {result} litres")