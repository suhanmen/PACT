# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # Each car is represented by its starting position
    left_cars = list(range(n))
    right_cars = list(range(2*n, n+2*n))

    # Initialize collision count to zero
    collisions = 0

    # Simulate the cars' movement
    for i in range(n):
        # Calculate each car's current position
        left_pos = left_cars[i] + i
        right_pos = right_cars[i] - i

        # Check if there is a collision at this position
        if left_pos >= right_pos:
            collisions += 1

    return collisions
