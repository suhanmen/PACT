def minPath(grid, k):
    n = len(grid)
    heap = [(grid[i][j], [i, j], [grid[i][j]]) for i in range(n) for j in range(n)]
    heapq.heapify(heap)
    visited = set()
    while heap:
        _, curr_pos, curr_path = heapq.heappop(heap)
        if len(curr_path) == k:
            return curr_path
        if tuple(curr_pos) in visited:
            continue
        visited.add(tuple(curr_pos))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_pos = [curr_pos[0] + dx, curr_pos[1] + dy]
            if 0 <= next_pos[0] < n and 0 <= next_pos[1] < n:
                next_val = grid[next_pos[0]][next_pos[1]]
                next_path = curr_path + [next_val]
                heapq.heappush(heap, (next_val, next_pos, next_path))
