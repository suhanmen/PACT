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
    # We assume that each car is at position 0 initially.
    # We also assume that each car moves one unit per second.
    # The time it takes for two cars to meet is simply the distance between them.
    # The total distance between two cars is 2n, since each car is n units apart.
    # Therefore, the time it takes for two cars to meet is 2n seconds.
    # In 2n seconds, each car will travel 2n units (n units in one direction and n units in the other direction).
    # Therefore, the collision point will be at position n.
    # We can count the number of collisions by counting the number of cars that are at position n.
    # Since each set of cars moves in opposite directions, we only need to check one set.
    return n
