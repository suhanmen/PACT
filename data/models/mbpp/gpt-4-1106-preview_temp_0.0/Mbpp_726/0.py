"""
Write a function that takes as input a tuple of numbers (t_1,...,t_{N+1}) and returns a tuple of length N where the i-th element of the tuple is equal to t_i * t_{i+1}.
assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
"""



def multiply_elements(input_tuple):
    # Initialize an empty list to store the results
    result = []
    # Iterate over the input tuple except the last element
    for i in range(len(input_tuple) - 1):
        # Multiply the current element with the next one and append to the result list
        result.append(input_tuple[i] * input_tuple[i + 1])
    # Convert the result list to a tuple and return it
    return tuple(result)

# Example usage
# assert multiply_elements((1, 5, 7, 8, 10)) == (5, 35, 56, 80)
