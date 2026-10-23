import math
import random


random.seed(6)
scores = [random.randint(1, 20) for _ in range(8)]

minimax_leaves = 0
alphabeta_leaves = 0

# 5.1 Minimax  (with leaf-evaluation counter)

def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
    global minimax_leaves
    # Base case: targetDepth reached
    if curDepth == targetDepth:
        minimax_leaves += 1
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
        )
    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
        )

# 5.2 Alpha-Beta Pruning  (with leaf-evaluation counter)

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global alphabeta_leaves
    if depth == target:
        alphabeta_leaves += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')
        for i in range(2):
            value = max(value, alphabeta(depth + 1, index * 2 + i, False, scores, target, alpha, beta))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for i in range(2):
            value = min(value, alphabeta(depth + 1, index * 2 + i, True, scores, target, alpha, beta))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value


def run_both(leaf_list):
    global minimax_leaves, alphabeta_leaves
    depth = int(math.log2(len(leaf_list)))
    minimax_leaves = 0
    alphabeta_leaves = 0
    mm = minimax(0, 0, True, leaf_list, depth)
    ab = alphabeta(0, 0, True, leaf_list, depth, float('-inf'), float('inf'))
    return mm, ab, minimax_leaves, alphabeta_leaves


def root_action(leaf_list):
    depth = int(math.log2(len(leaf_list)))
    left = minimax(1, 0, False, leaf_list, depth)
    right = minimax(1, 1, False, leaf_list, depth)
    return ("Left (A)" if left >= right else "Right (B)"), left, right


def alphabeta_trace(depth, index, maxTurn, scores, target, alpha, beta, name="Root"):
    pad = "  " * depth
    kind = "MAX" if maxTurn else "MIN"
    if depth == target:
        print(f"{pad}Leaf {name}: value = {scores[index]}")
        return scores[index]
    print(f"{pad}Visit {name} ({kind})  alpha={alpha}  beta={beta}")
    if maxTurn:
        value = float('-inf')
        for i in range(2):
            child = name + ("L" if i == 0 else "R")
            value = max(value, alphabeta_trace(depth + 1, index * 2 + i, False, scores, target, alpha, beta, child))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"{pad}  PRUNE after {child}: alpha={alpha} >= beta={beta}")
                break
        print(f"{pad}Return {name} = {value}")
        return value
    else:
        value = float('inf')
        for i in range(2):
            child = name + ("L" if i == 0 else "R")
            value = min(value, alphabeta_trace(depth + 1, index * 2 + i, True, scores, target, alpha, beta, child))
            beta = min(beta, value)
            if alpha >= beta:
                print(f"{pad}  PRUNE after {child}: alpha={alpha} >= beta={beta}")
                break
        print(f"{pad}Return {name} = {value}")
        return value



def reorder(leaf_list, mask):
    depth = int(math.log2(len(leaf_list)))

    def build(d, idx):
        if d == depth:
            return [leaf_list[idx]]
        heap_id = (1 << d) - 1 + idx          # unique id of internal node
        a = build(d + 1, idx * 2)
        b = build(d + 1, idx * 2 + 1)
        return (b + a) if (mask >> heap_id) & 1 else (a + b)

    return build(0, 0)


treeDepth = int(math.log2(len(scores)))

print("=" * 60)
print("TASK 1: Minimax hand-trace tree")
print("=" * 60)
print("Leaf scores :", scores)
print("Tree depth  :", treeDepth)
# bottom-up values
lvl2 = [max(scores[0], scores[1]), max(scores[2], scores[3]),
        max(scores[4], scores[5]), max(scores[6], scores[7])]
lvl1 = [min(lvl2[0], lvl2[1]), min(lvl2[2], lvl2[3])]
print("Level 2 (MAX nodes) :", lvl2)
print("Level 1 (MIN nodes) :", lvl1)
print("Level 0 (MAX root)  :", max(lvl1))

print()
print("=" * 60)
print("TASK 2: Leaf-evaluation counters")
print("=" * 60)
mm, ab, c_mm, c_ab = run_both(scores)
print("The optimal value (Minimax)    is:", mm, "| leaves evaluated =", c_mm)
print("The optimal value (Alpha-Beta) is:", ab, "| leaves evaluated =", c_ab)
action, lv, rv = root_action(scores)
print(f"Root action: {action}  (Left MIN = {lv}, Right MIN = {rv})")
print("Values agree?", mm == ab)
print("Leaves saved:", c_mm - c_ab)

print()
print("Alpha-Beta step-by-step trace (original order):")
alphabeta_trace(0, 0, True, scores, treeDepth, float('-inf'), float('inf'))

print()
print("=" * 60)
print("TASK 3: Reordering branches (swap children of internal nodes)")
print("=" * 60)
results = []
for mask in range(2 ** (2 ** treeDepth - 1)):          # 2^7 = 128 orderings
    order = reorder(scores, mask)
    m, a, cm, ca = run_both(order)
    results.append((ca, mask, order, m, a))

best = min(results, key=lambda r: r[0])
worst = max(results, key=lambda r: r[0])

print(f"Total orderings tried : {len(results)}")
print(f"All minimax values equal {mm}? ", all(r[3] == mm and r[4] == mm for r in results))
print(f"Best  ordering : {best[2]}  -> alpha-beta leaves = {best[0]}  value = {best[4]}")
print(f"Worst ordering : {worst[2]}  -> alpha-beta leaves = {worst[0]}  value = {worst[4]}")
print(f"Original order : {scores}  -> alpha-beta leaves = {c_ab}  value = {ab}")

print()
print("Distribution of alpha-beta leaf counts over the 128 orderings:")
dist = {}
for r in results:
    dist[r[0]] = dist.get(r[0], 0) + 1
for k in sorted(dist):
    print(f"  {k} leaves : {dist[k]} orderings")

print()
print("Sample reorderings:")
samples = {
    "Original": scores,
    "Reversed (all swaps)": reorder(scores, 127),
    "Best": best[2],
    "Worst": worst[2],
}
print(f"{'Ordering':<22}{'Leaves':<28}{'MM value':<10}{'AB value':<10}{'MM leaves':<11}{'AB leaves'}")
for name, order in samples.items():
    m, a, cm, ca = run_both(order)
    print(f"{name:<22}{str(order):<28}{m:<10}{a:<10}{cm:<11}{ca}")

print()
print("=" * 60)
print("EDGE CASES / COMPARISON TESTS")
print("=" * 60)

# Edge 1: all leaves equal
t = [7] * 8
print("Edge 1 (all equal)      :", t, "->", run_both(t))

# Edge 2: negative values
t = [-5, -12, -3, -20, -8, -1, -9, -15]
print("Edge 2 (all negative)   :", t, "->", run_both(t))

# Edge 3: smallest tree (depth 1, 2 leaves)
t = [4, 11]
print("Edge 3 (depth 1)        :", t, "->", run_both(t))

# Edge 4: larger tree, 16 leaves
random.seed(21)
t = [random.randint(1, 50) for _ in range(16)]
print("Edge 4 (16 random leaves):", t, "->", run_both(t))

# Edge 5: 1000 random trees -> alpha-beta never worse, always same value
ok_value = True
ok_leaves = True
total_mm = total_ab = 0
random.seed(99)
for _ in range(1000):
    t = [random.randint(-50, 50) for _ in range(16)]
    m, a, cm, ca = run_both(t)
    ok_value &= (m == a)
    ok_leaves &= (ca <= cm)
    total_mm += cm
    total_ab += ca
print("Edge 5 (1000 random 16-leaf trees):")
print("   same value every time   :", ok_value)
print("   AB leaves <= MM leaves  :", ok_leaves)
print(f"   average leaves  MM = {total_mm / 1000:.1f}   AB = {total_ab / 1000:.1f}")

# Limitation: padding with 0 (from manual 5.1) can change the answer
print()
print("Limitation test (padding with 0 as in manual 5.1):")
t = [6, 9, 4, 8, 7]                 # 5 leaves, not a power of 2
d = math.ceil(math.log2(len(t)))
padded = t + [0] * (2 ** d - len(t))
print("   Original leaves :", t)
print("   Padded leaves   :", padded)
print("   Minimax on padded tree =", minimax(0, 0, True, padded, d),
      "(fake 0 leaves can affect the MIN nodes, so padding must be chosen carefully)")
