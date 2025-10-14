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
    # We can compute the number of collisions as the number of pairs of cars
    # that have opposite directions and are moving towards each other.
    # The first car from the left-to-right set will collide with the first car
    # from the right-to-left set, the second with the second, and so on.
    # Therefore, the total number of collisions is n * (n - 1) / 2.
    return n * (n - 1) // 2
