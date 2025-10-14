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
    # We can model the cars as points moving along a straight line.
    # Let the left-to-right cars have initial positions 1, 2, ..., n.
    # Let the right-to-left cars have initial positions -1, -2, ..., -n.
    # All cars have the same speed, so they cover the same distance in the same time.
    # We can assume that the time is measured in such a way that the distance covered is 1.

    # We can use a set to keep track of the positions of the right-to-left cars.
    # Initially, all positions are present.
    right_to_left = set(range(-n, 0))

    # We can iterate over the positions of the left-to-right cars.
    # For each position, we check if there is a right-to-left car at the same position.
    # If there is, we count a collision and remove the right-to-left car from the set.
    collisions = 0
    for i in range(1, n+1):
        if -i in right_to_left:
            collisions += 1
            right_to_left.remove(-i)

    return collisions
