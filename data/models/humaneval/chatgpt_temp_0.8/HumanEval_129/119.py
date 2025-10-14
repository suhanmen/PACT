def minPath(grid, k):
    n = len(grid)
    start = [(i, j) for i in range(n) for j in range(n)]
    start.sort(key=lambda pos: grid[pos[0]][pos[1]])
    visited = set()
    queue = [(pos, [grid[pos[0]][pos[1]]]) for pos in start]
    while queue:
        pos, path = queue.pop(0)
        if len(path) == k:
            return path
        if pos in visited:
            continue
        visited.add(pos)
        for neighbor in [(pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)]:
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < n:
                queue.append((neighbor, path + [grid[neighbor[0]][neighbor[1]]]))
    return None
