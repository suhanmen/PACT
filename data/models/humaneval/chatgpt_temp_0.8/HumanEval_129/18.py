import heapq

def minPath(grid, k):
    n = len(grid)

    def get_value(coords):
        i, j = coords
        return grid[i][j]

    def get_neighbors(coords):
        i, j = coords
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if i < n - 1:
            neighbors.append((i + 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if j < n - 1:
            neighbors.append((i, j + 1))
        return neighbors

    heap = []
    for i in range(n):
        for j in range(n):
            heapq.heappush(heap, (get_value((i, j)), [(i, j)]))

    while heap:
        value, path = heapq.heappop(heap)
        if len(path) == k:
            return [get_value(coords) for coords in path]
        last_coords = path[-1]
        for coords in get_neighbors(last_coords):
            if coords not in path:
                new_path = path + [coords]
                new_value = [get_value(coords) for coords in new_path]
                heapq.heappush(heap, (new_value, new_pat
