def sort_array(arr):
    # Define a helper function to count the number of ones in binary representation of a number
    def count_ones(n):
        return bin(n).count('1')

    # Use the helper function and a lambda function to sort the array
    return sorted(arr, key=lambda x: (count_ones(x), x))
