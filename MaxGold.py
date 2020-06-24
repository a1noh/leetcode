def getMaximumGold(grid):
    if grid is None:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    b = [[False for i in range(cols)] for j in range(rows)]
    m = 0
    for row in range(rows):
        for col in range(cols):
            if (grid[row][col] != 0):
                # print(grid[row][col])
                cur = traverse(grid, row, col, rows, cols, b)
                m = max(m, cur)
    print(m)


def traverse(grid, row, col, maxRow, maxCol, b):
    if row < 0 or col < 0 or row >= maxRow or col >= maxCol or b[row][col] is True or grid[row][col] == 0:
        return 0
    b[row][col] = True
    left = traverse(grid, row, col -1, maxRow, maxCol, b)
    right = traverse(grid, row, col +1, maxRow, maxCol, b)
    up = traverse(grid, row - 1, col, maxRow, maxCol, b)
    down = traverse(grid, row + 1, col, maxRow, maxCol, b)
    b[row][col] = False
    #print(left, right, up, down)
    num = max(left, max(right, max(up, down)))
    num += grid[row][col]
    return num


getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]])
