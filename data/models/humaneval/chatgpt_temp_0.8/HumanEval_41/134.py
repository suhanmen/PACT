# CANNOT PARSE CODE SNIPPET
python
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
    # We can represent the cars as points on the line, where the position is the time
    # it takes for the car to reach the end of the road. For example, a car starting
    # at position 0 and moving left to right with speed 1 would have position t = x/1,
    # where x is the distance it has traveled in time t.
    
    # We can define two lists to represent the positions of the left-to-right and
    # right-to-left cars respectively. We initialize them to be 1 and -1, which
    # correspond to the two ends of the road.
    left_to_right = [1 for _ in range(n)]
    right_to_left = [-1 for _ in range(n)]
    
    # We will iterate over time t, and check if any cars collide at each time step.
    collisions = 0
    for t in range(1, n+1):
        # To check if two cars collide, we can simply see if their positions overlap:
        for i in range(n):
            if left_to_right[i] == right_to_left[i]:
                collisions += 1
        
        # We update the positions of all cars for the next time step:
        for i in range(n):
            left_to_right[i] += 1
            right_to_left[i] -= 1
    
    return collisions
