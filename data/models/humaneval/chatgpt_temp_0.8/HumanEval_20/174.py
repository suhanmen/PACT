from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Initialize variables to keep track of the closest pair of numbers found so far
    closest_pair = (numbers[0], numbers[1])
    closest_distance = abs(numbers[0] - numbers[1])
    
    # Loop through all pairs of numbers in the list
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Calculate the distance between the current pair of numbers
            distance = abs(numbers[i] - numbers[j])
            
            # Update the closest pair and distance if the current pair is closer
            if distance < closest_distance:
                closest_pair = (numbers[i], numbers[j])
                closest_distance = distance
                
    # Return the closest pair in order (smaller number first)
    return tuple(sorted(closest_pair))
