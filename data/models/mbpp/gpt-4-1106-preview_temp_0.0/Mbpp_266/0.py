"""
Write a function to find the lateral surface area of a cube given its side length.
assert lateralsurface_cube(5)==100
"""



def lateralsurface_cube(side_length):
    # There are 4 lateral faces in a cube, each with an area of side_length^2
    lateral_surface_area = 4 * (side_length ** 2)
    return lateral_surface_area

# Test the function
assert lateralsurface_cube(5) == 100
