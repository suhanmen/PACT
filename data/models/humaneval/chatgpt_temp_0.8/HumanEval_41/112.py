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
    # We can assume that the left-to-right cars are all faster than the right-to-left cars.
    # Otherwise, they would eventually collide head-on, which is not allowed.
    # So we can sort the speeds of the cars and consider them in decreasing order.
    speeds = list(range(1, n+1))
    speeds.sort(reverse=True)

    # We can count the number of collisions by iterating through the speeds
    # and computing the distance between the leftmost left-to-right car
    # and the rightmost right-to-left car that is moving faster than it.
    # If the distance is less than or equal to zero, then a collision happens.
    collisions = 0
    for i in range(n):
        distance = i + 1 + n - speeds[i]
        if distance <= 0:
            collisions += 1

    return collisions
