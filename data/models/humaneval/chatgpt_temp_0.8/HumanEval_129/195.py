from heapq import heappush, heappop

def minPath(grid, k):
    # Define directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Define heap to store possible paths
    heap = []
    
    # Add all cells to heap
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            heappush(heap, (grid[i][j], [(i, j)]))
            
    # Visit cells while keeping track of the path
    while heap:
        curr_val, curr_path = heappop(heap)
        if len(curr_path) == k:
            return [grid[i][j] for i, j in curr_path]
        curr_cell = curr_path[-1]
        for dx, dy in directions:
            new_x, new_y = curr_cell[0] + dx, curr_cell[1] + dy
            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]):
                new_path = curr_path + [(new_x, new_y)]
                heappush(heap, (grid[new_x][new_y], new_path))
