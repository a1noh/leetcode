def cycleInGraph(edges):
    # Write your code here.
    visted = [0 for _ in range(len(edges))]
    curStack = [0 for _ in range(len(edges))]

    for i in range(len(edges)):
        if visted[i]:
            continue
        if dfs(edges, i, visted, curStack):
            return True
    return False


def dfs(edges, i, visted, curStack):
    visted[i] = 1
    curStack[i] = 1

    for neighbor in edges[i]:
        if visted[neighbor] == 0:
            if dfs(edges, neighbor, visted, curStack):
                return True
        elif curStack[neighbor] == 1:
            return True
    curStack[i] = 0
    return False


