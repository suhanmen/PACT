# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
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
    # Each car has a unique ID which is its position on the road
    # For each left car, we calculate the position where it would meet a right car
    # If the position is valid, add it to the set of all possible collision positions
    colliding_positions = set()
    for i in range(n):
        right_car_position = (i + 1) * -1
        collision_position = right_car_position - i
        if collision_position > 0:
            colliding_positions.add(collision_position)
    # We then iterate through all right cars, checking if any of them collide
    # with a left car at one of the possible collision positions
    collisions = 0
    for i in range(n):
        right_car_position = i + 1
        if right_car_position in colliding_positions:
            collisions += 1
    return collisions
