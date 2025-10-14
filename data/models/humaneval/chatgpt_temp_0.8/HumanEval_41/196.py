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
    # We can solve this problem by computing the number of pairs of cars that
    # can collide. Each car moving left to right can collide with any car moving
    # right to left that is to its right (i.e., has a later starting position).
    # Therefore, the number of collisions is the number of such pairs of cars.
    # If we assume that the cars start at positions 1 to n (left to right) and
    # n+1 to 2n (right to left), then the ith car moving left to right can
    # collide with the (n+1)-th to the (n+i)-th car moving right to left.
    # Therefore, the total number of collisions is the sum of the numbers
    # n+1 to 2n-i for i from 1 to n.
    # We can simplify this formula to 3n(n+1)/2 - n.

    return 3 * n * (n + 1) // 2 - n
