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
    # The distance between each car
    car_distance = 100

    # The speed of each car
    car_speed = 10

    # The time it takes for each car to reach the end of the road
    time_to_end = car_distance / car_speed

    # The total time it takes for the two sets of cars to collide or reach the end of the road
    total_time = 2 * time_to_end

    # The number of collisions is equal to the number of cars travelling in each direction
    num_collisions = n * n

    # The probability of a collision is the number of collisions divided by the total possible combinations
    # of cars travelling in opposite directions
    prob_collision = num_collisions / (n * (n - 1))

    # The expected number of collisions is the probability of a collision multiplied by the total time
    expected_collisions = prob_collision * total_time

    return expected_collisions
