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
    # We can represent the position of each car as a single number, where
    # positive numbers represent left-to-right cars and negative numbers
    # represent right-to-left cars. Specifically, the i-th left-to-right car
    # starts at position i, and the i-th right-to-left car starts at position
    # -i. This way, we know that two cars collide when their positions sum up
    # to zero.

    num_collisions = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j == 0:
                num_collisions += 1

    return num_collisions
