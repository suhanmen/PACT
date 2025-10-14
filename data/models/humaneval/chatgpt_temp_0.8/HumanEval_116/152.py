def sort_array(arr):
    # Function to count the number of ones in binary representation of a number
    def count_ones(num):
        return bin(num).count('1')
    
    # Sort the array based on the number of ones and decimal value
    return sorted(arr, key=lambda x: (count_ones(x), x))
