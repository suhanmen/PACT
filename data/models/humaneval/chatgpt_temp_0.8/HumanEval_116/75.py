def sort_array(arr):
    # Helper function to get the number of ones in binary representation of a number
    def get_num_ones(n):
        return bin(n).count('1')
    
    # Sort the array based on the number of ones in binary representation
    # If the number of ones is same, sort based on decimal value
    return sorted(arr, key=lambda x: (get_num_ones(x), x))
