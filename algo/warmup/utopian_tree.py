def grow_tree(tree, current_cycle, total_cycles):
    if (total_cycles == 0):
        return tree

    if (current_cycle % 2 == 0):
        tree = tree + 1
    else:
        tree = tree * 2

    if (current_cycle == total_cycles):
        return tree
    else:
        return grow_tree(tree, current_cycle + 1, total_cycles)

t = int(raw_input())
for i in range(0, t):
    initial_tree = 1
    total_cycles = int(raw_input())
    print grow_tree(initial_tree, 1, total_cycles)
