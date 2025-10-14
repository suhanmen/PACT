# CANNOT PARSE CODE SNIPPET
def car_race_collision(n: int) -> int:
    # Each car is represented by its position on the road
    # We will maintain two lists of positions for the cars going in opposite directions
    left_to_right = [i for i in range(n)]
    right_to_left = [i for i in range(n, 2 * n)]

    # We will use two pointers to iterate through the sorted lists of positions
    # The i-th car going left to right corresponds to the i-th position in the left_to_right list
    # The j-th car going right to left corresponds to the j-th position in the right_to_left list
    i = j = 0

    # Count the number of collisions
    num_collisions = 0

    while i < n and j < n:
        # If the i-th car is behind the j-th car, move the i-th car forward
        if left_to_right[i] < right_to_left[j]:
            i += 1
        # If the i-th car is ahead of or at the same position as the j-th car, there is a collision
        else:
            num_collisions += 1
            j += 1

    return num_collisions
