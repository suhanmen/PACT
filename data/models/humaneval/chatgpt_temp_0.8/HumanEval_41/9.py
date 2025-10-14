# CANNOT PARSE CODE SNIPPET
python
def car_race_collision(n: int) -> int:
    # Initialize the positions of the left-moving and right-moving cars
    left_cars = [i for i in range(n)]
    right_cars = [i for i in range(n, 2*n)]
    
    # Keep track of the number of collisions
    num_collisions = 0
    
    # Simulate the movement of the cars until they are all out of sight
    while left_cars[-1] < right_cars[0]:
        # Check if there is a collision between the first left-moving car and
        # the last right-moving car
        if left_cars[0] + right_cars[-1] == 2*n - 1:
            num_collisions += 1
        
        # Move all cars one unit to the right
        left_cars = [pos+1 for pos in left_cars]
        right_cars = [pos-1 for pos in right_cars]
    
    return num_collisions
