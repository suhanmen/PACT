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
    # We can represent the positions of the cars as two lists of length n.
    # Let's say that the i-th car driving left to right starts at position L[i],
    # and the i-th car driving right to left starts at position R[i].
    # For simplicity, let's assume L[i] > R[i] for all i.

    L = [2 * i for i in range(n)]  # Even numbers starting at 0
    R = [2 * i + 1 for i in range(n)]  # Odd numbers starting at 1

    # We can iterate over the positions of the left-to-right cars,
    # and for each position i, count how many right-to-left cars are
    # at positions less than i. This will give us the number of collisions
    # that happen at position i.

    collisions = 0
    for i in L:
        for j in R:
            if j < i:
                collisions += 1

    return collisions
