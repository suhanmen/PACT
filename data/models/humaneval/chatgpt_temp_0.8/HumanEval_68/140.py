def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0]  # List comprehension to find even values in the array
    
    if not even_values:  # Return empty list if no even values found
        return []
    
    smallest_even = min(even_values)  # Find the smallest even value
    smallest_even_indices = [i for i, num in enumerate(arr) if num == smallest_even and num % 2 == 0]  # List comprehension to find indices of smallest even value
    
    return [smallest_even, smallest_even_indices[0]]  # Return smallest even value and its smallest index
