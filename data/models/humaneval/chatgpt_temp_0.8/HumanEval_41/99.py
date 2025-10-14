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
    # We can think of the left-moving cars as starting at position 0 and moving positively,
    # while the right-moving cars start at position n-1 and move negatively.
    # Let's create two lists to store the positions of each set of cars.
    left_cars = list(range(n))
    right_cars = list(range(n-1, -1, -1))  # start at n-1, end at -1 (exclusive), step by -1

    # Keep track of the number of collisions.
    num_collisions = 0

    # We iterate until the two sets of cars pass each other, i.e. until the leftmost
    # left-moving car passes the rightmost right-moving car.
    while left_cars[-1] < right_cars[0]:
        # Check if there is a collision at the current time step.
        if left_cars[0] >= right_cars[0]:
            num_collisions += 1

        # Update the positions of the cars for the next time step.
        for i in range(n):
            left_cars[i] += 1
            right_cars[i] -= 1

    return num_collisions
