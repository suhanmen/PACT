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
    # The number of collisions is equal to the number of pairs of cars that are moving towards each other.
    # We can count the number of such pairs by computing the number of ways to choose 2 cars from each set.
    # This is equivalent to the product of the binomial coefficients (n choose 2).
    return n * (n - 1)
