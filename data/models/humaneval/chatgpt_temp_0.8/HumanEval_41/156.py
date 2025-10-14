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
    # Each car has a unique speed, starting position, and direction (left or right)
    # We can represent each car as a tuple of (speed, position, direction)
    cars_ltr = [(i+1, i, "right") for i in range(n)]
    cars_rtl = [(i+1, i+2*n, "left") for i in range(n)]
    # Initialize the total number of collisions to 0
    total_collisions = 0
    # Loop through all possible pairs of cars
    for car1 in cars_ltr:
        for car2 in cars_rtl:
            if car1[2] == "right" and car2[2] == "left":
                # Calculate the time it takes for the two cars to collide
                t_collision = (car2[1] - car1[1]) / (car1[0] + car2[0])
                # If the time is positive and less than infinity, the cars will collide
                if t_collision > 0 and t_collision < float('inf'):
                    total_collisions += 1
                    # Print information about the collision
                    print(f"Collision between car {car1[0]} going right and car {car2[0]} g
