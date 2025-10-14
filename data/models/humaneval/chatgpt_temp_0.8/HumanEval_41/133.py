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
    # We can assume that the distance between each pair of cars is 1.
    # The cars on one side of the road will have positions 0, 1, 2, ..., n-1.
    # The cars on the other side of the road will have positions n, n+1, n+2, ..., 2n-1.
    # A collision will occur if and only if the positions of two cars sum up to an even number.
    # We can count the number of such pairs of positions using combinatorics.

    # Count the total number of collisions by summing the number of collisions for each car on the left side.
    total_collisions = 0
    for i in range(n):
        # The i-th car on the left side has position i.
        # The number of cars on the right side that can collide with it is n-i.
        # We need to count the number of even sums between i and the positions of the cars on the right side.
        # This is equivalent to counting the number of odd numbers between n+i and 2n-1.
        # The formula for that is ((2n-1) - (n+i)) // 2 + 1 = 2n-i-1 // 2 - (n+i) % 2.
        total_collisions += (2*n-i-1) // 2 - (n+i) % 2

    return total_collisions
