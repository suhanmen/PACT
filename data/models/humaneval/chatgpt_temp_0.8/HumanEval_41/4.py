# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # Each car can be identified by its position on the road
    # We will represent left-moving cars with negative positions and right-moving cars with positive positions
    left_cars = set(range(-n, 0))
    right_cars = set(range(1, n+1))
    # Initialize the number of collisions to 0
    collisions = 0
    # Continue simulating the cars until they are all off the road
    while left_cars and right_cars:
        # Calculate the distance between the closest left-moving car and the closest right-moving car
        closest_distance = min(abs(car1 - car2) for car1 in left_cars for car2 in right_cars)
        # If the closest distance is 1, there is a collision
        if closest_distance == 1:
            collisions += 1
        # Move all cars simultaneously in their respective directions
        left_cars = {car + 1 for car in left_cars}
        right_cars = {car - 1 for car in right_cars}
    return collisions
