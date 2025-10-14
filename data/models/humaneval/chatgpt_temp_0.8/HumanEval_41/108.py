# CANNOT PARSE CODE SNIPPET
python
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
    # Each pair of cars has a chance to collide, so there are n^2 possible collisions.
    # However, we must remove collisions where both cars are moving in the same direction.
    same_direction_collisions = n * (n - 1)  # n choices for the first car, n-1 for the second
    total_collisions = n ** 2 - same_direction_collisions
    return total_collisions
