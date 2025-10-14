def pluck(arr):
    even_values = [num for num in arr if num % 2 == 0] # get all even values
    if not even_values: # if no even values, return empty list
        return []
    else:
        smallest_even = min(even_values) # get the smallest even value
        smallest_even_indices = [i for i,num in enumerate(arr) if num == smallest_even] # get the indices of the smallest even value
        return [smallest_even, smallest_even_indices[0]] # return the smallest even value and its smallest index
