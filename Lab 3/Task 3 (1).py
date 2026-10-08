# Depth-Limited Search (DLS) and Iterative Deepening DFS (IDDFS)
# Root is at depth 0. Cycle check is path-local (only checks the current path).

FOUND = "FOUND"
CUTOFF = "CUTOFF"
FAILURE = "FAILURE"

# Graph (directed, neighbours are tried in the listed order)
# A -> B is depth 1, A -> B -> D is depth 2, and so on.
# B -> A and G -> C are back edges, so the graph has cycles.
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["F", "G"],
    "D": ["H"],
    "E": ["I"],
    "F": ["J"],
    "G": ["C", "K"],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
}

START = "A"
GOAL = "K"

expanded = 0   # counts how many nodes were expanded (used to show repeated work)


def dls_recursive(node, goal, limit, depth, path):
    """Returns (status, path). path is the list of nodes from the root to node."""
    global expanded
    expanded += 1

    if node == goal:
        return FOUND, list(path)

    if depth == limit:
        return CUTOFF, None          # cannot go deeper, but maybe the goal is below

    cutoff_occurred = False
    for child in graph[node]:
        if child in path:            # path-local cycle check
            continue                 # skip this child, it is a cycle (not a cutoff)
        path.append(child)
        status, result = dls_recursive(child, goal, limit, depth + 1, path)
        path.pop()                   # go back (backtrack)
        if status == FOUND:
            return FOUND, result
        if status == CUTOFF:
            cutoff_occurred = True   # remember it, but keep trying other children

    if cutoff_occurred:
        return CUTOFF, None
    return FAILURE, None             # everything below was searched, no goal


def dls(start, goal, limit):
    """Runs one depth-limited search. Returns (status, path, nodes_expanded)."""
    global expanded
    expanded = 0
    status, path = dls_recursive(start, goal, limit, 0, [start])
    return status, path, expanded


def iddfs(start, goal, max_depth):
    """Tries limits 0,1,2,... up to max_depth.
    Returns (status, path, limits_attempted, total_expanded, expanded_per_limit)."""
    attempted = []
    per_limit = []
    total = 0
    status = CUTOFF
    path = None
    for limit in range(0, max_depth + 1):
        attempted.append(limit)
        status, path, count = dls(start, goal, limit)
        per_limit.append(count)
        total += count
        if status == FOUND:
            return FOUND, path, attempted, total, per_limit
        if status == FAILURE:         # whole graph searched, no need to go deeper
            return FAILURE, None, attempted, total, per_limit
    return status, path, attempted, total, per_limit   # CUTOFF: max depth reached


def show_path(path):
    return " -> ".join(path) if path else "None"


if __name__ == "__main__":
    print("Start =", START, " Goal =", GOAL, " (root depth = 0)\n")

    print("=== DLS ===")
    print(f"{'Limit':<6}{'Status':<10}{'Nodes expanded':<16}Path")
    for limit in [1, 2, 3, 4]:
        status, path, count = dls(START, GOAL, limit)
        print(f"{limit:<6}{status:<10}{count:<16}{show_path(path)}")

    print("\n=== IDDFS ===")
    print(f"{'Max depth':<10}{'Status':<10}{'Limits attempted':<20}{'Total expanded':<16}Path")
    for m in [1, 2, 3, 4]:
        status, path, att, total, per = iddfs(START, GOAL, m)
        print(f"{m:<10}{status:<10}{str(att):<20}{total:<16}{show_path(path)}")

    print("\n=== Expanded nodes per limit inside IDDFS (max depth 4) ===")
    status, path, att, total, per = iddfs(START, GOAL, 4)
    for l, c in zip(att, per):
        print(f"limit {l}: {c} nodes expanded")
    print("total:", total)

    print("\n=== Extra test: goal Z is not in the graph (shows FAILURE) ===")
    for limit in [3, 4]:
        status, path, count = dls(START, "Z", limit)
        print(f"DLS limit {limit}: {status}, expanded {count}")
