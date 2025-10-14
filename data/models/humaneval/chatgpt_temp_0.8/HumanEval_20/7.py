def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # initialize the variables for the closest pair of numbers
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_distance = sorted_numbers[1] - sorted_numbers[0]
    
    # iterate over the list and update the closest pair if a smaller distance is found
    for i in range(1, len(sorted_numbers) - 1):
        distance = sorted_numbers[i+1] - sorted_numbers[i]
        if distance < min_distance:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_distance = distance
    
    return closest_pair
