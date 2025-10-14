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

    # Initialize an empty set to keep track of collisions
    collisions = set()

    # Iterate through each car moving left to right
    for i in range(n):
        # Calculate the position of the car at time t
        position = i * 100 + 50
        # For each car moving right to left, check if they will collide
        for j in range(n):
            # Calculate the position of the car at time t
            position2 = j * 100 + 50
            # If the positions match, add them to the set of collisions
            if position == position2:
                collisions.add((i,j))

    # Return the number of collisions
    return len(collisions)
