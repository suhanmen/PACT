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
    # We can simulate the movement of the cars without actually moving them.
    # Suppose we have a list of n integers representing the positions of the left-to-right cars,
    # and a list of n integers representing the positions of the right-to-left cars.
    # We can sort these lists and compare the positions of the cars in pairs.
    # If a left-to-right car is at position x and a right-to-left car is at position y,
    # and x < y, then these cars will collide.
    # We can count the number of collisions and return that count.
    
    # Create two lists of n random positions for the cars.
    ltr_cars = [random.randint(0, 100) for _ in range(n)]
    rtl_cars = [random.randint(101, 200) for _ in range(n)]
    
    # Sort the lists in ascending order.
    ltr_cars.sort()
    rtl_cars.sort()
    
    # Count the number of collisions.
    count = 0
    for i in range(n):
        if ltr_cars[i] < rtl_cars[i]:
            count += 1
            
    return count
