def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # We can think of each car as a point moving along a line, with the direction
    # it's moving as a binary value (0 = left to right, 1 = right to left).
    # If we sort these points by their position on the line, we can iterate through
    # them in order and count the number of collisions as we go.
    # We can use a list of tuples to keep track of each car's position and direction.

    # Initialize lists of left-moving and right-moving cars
    left_cars = [(i, 0) for i in range(n)]  # (position, direction)
    right_cars = [(i, 1) for i in range(n, 2*n)]

    # Combine the two lists and sort by position
    all_cars = left_cars + right_cars
    all_cars.sort()

    # Now we can iterate through the list of cars and count collisions
    collisions = 0
    for i in range(len(all_cars)):
        pos_i, dir_i = all_cars[i]
        for j in range(i+1, len(all_cars)):
            pos_j, dir_j = all_cars[j]
            if dir_i != dir_j and pos_j - pos_i <= 1:
                collis
