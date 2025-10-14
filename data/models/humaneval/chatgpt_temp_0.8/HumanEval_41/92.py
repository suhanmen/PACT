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
    # We can think of the problem as if the right-moving cars are stationary,
    # and the left-moving cars are moving towards them.
    # We can simply count the number of times a left-moving car passes a right-moving car,
    # since that's when a collision happens.
    # Each left-moving car is equally likely to pass any of the right-moving cars,
    # so we can use the formula for combinations to count the number of possible collisions.
    # Specifically, the total number of possible collisions is n choose 2 (i.e., nC2).
    # This is because we're choosing 2 left-moving cars out of n to collide,
    # and there are n choose 2 ways to do that.

    return n * (n - 1) // 2
