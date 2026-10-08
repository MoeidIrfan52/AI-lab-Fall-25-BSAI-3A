# Task 3: Thermostat agent with memory of the previous mode
# Existing rules kept:
#   temp < 18        -> HEAT
#   temp > 26        -> COOL
#   18 <= temp <= 26 -> OFF   (so 18 and 26 exactly are OFF)
#   room empty       -> OFF   (occupancy has priority over temperature)
# New: the agent remembers the last target mode and only sends a command
# when the target is different from it.

LOW = 18
HIGH = 26


class ThermostatAgent:
    def __init__(self):
        self.prev_mode = None      # nothing sent yet

    def decide(self, temperature, occupied):
        """Old logic: returns the target mode only."""
        if not occupied:           # occupancy priority
            return "OFF"
        if temperature < LOW:
            return "HEAT"
        if temperature > HIGH:
            return "COOL"
        return "OFF"

    def act(self, percept):
        """Returns (target, send_command)."""
        temperature, occupied = percept
        target = self.decide(temperature, occupied)
        send_command = (target != self.prev_mode)
        self.prev_mode = target    # update memory
        return target, send_command


if __name__ == "__main__":
    agent = ThermostatAgent()

    # (description, (temperature, occupied))
    tests = [
        ("first percept, cold",      (15, True)),
        ("repeat same percept",      (15, True)),
        ("repeat again",             (15, True)),
        ("exact lower boundary 18",  (18, True)),
        ("repeat boundary 18",       (18, True)),
        ("exact upper boundary 26",  (26, True)),
        ("transition: hot",          (30, True)),
        ("repeat hot",               (30, True)),
        ("transition: cold",         (10, True)),
        ("empty room, cold",         (10, False)),
        ("empty room, hot",          (35, False)),
        ("room occupied again, hot", (35, True)),
    ]

    header = f"{'No':<3} {'Case':<26} {'Prev mode':<10} {'Percept (T, occ)':<18} {'Target':<7} Command"
    print(header)
    print("-" * len(header))
    for i, (name, percept) in enumerate(tests, 1):
        prev = agent.prev_mode
        target, send = agent.act(percept)
        outcome = f"SEND {target}" if send else "no command"
        print(f"{i:<3} {name:<26} {str(prev):<10} {str(percept):<18} {target:<7} {outcome}")
