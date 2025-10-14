"""
Write a function to extract all the adjacent coordinates of the given coordinate tuple.
assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]]
"""



def get_coordinates(coord):
    x, y = coord
    adjacent_coords = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) != coord:
                adjacent_coords.append([i, j])
    return adjacent_coords

# Example usage:
# assert get_coordinates((3, 4)) == [[2, 3], [2, 4], [2, 5], [3, 3], [3, 5], [4, 3], [4, 4], [4, 5]]
